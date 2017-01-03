#! /usr/bin/env python
'''
Siavash Mirarab 2016

Compute tree shape probabilities

'''
# imports
import sys
from numpy.random import exponential
import dendropy

USAGE_MESSAGE = '''
USAGE: python ComputeProb.py <rateA> <rateB> <tree> <type>
    -rateA: (A)ctivation Rate, rate at which inactive Alus create offspring
    -rateB: (B)irth Rate, rate at which active Alus create offspring
    -tree:  A file with trees to be scored
    -type:  0: ordered ranked, 1: unordered ranked, 2: unordered unranked
'''

def computeProbUnrank(r, t):
    t.ladderize() # ladderize to make equivalent subtrees identical
    sigma = 0     # count number of symmetric nodes
    n = len(t.leaf_nodes()) # n = number of leaves

    # compute min_rank numbers for all nodes (min_rank = # edges to root) and symmetric nodes
    for node in t.preorder_node_iter():
        if node.parent_node is None:
            node.min_rank = 0
        else:
            node.min_rank = node.parent_node.min_rank + 1
        if symmetric_subtree(node):
            sigma += 1

    # compute rankings
    for node in t.postorder_node_iter():
        ch = node.child_nodes()
        if node.is_leaf(): # leaves
            node.phi = []
        elif ch[0].is_leaf() and ch[1].is_leaf(): # cherry parent
            node.phi = [{node:i} for i in range(node.min_rank,n-1)]
        elif ch[0].is_leaf(): # left child leaf, right child not leaf
            node.phi = []
            for phi in ch[1].phi:
                child_rank = phi[ch[1]]
                for i in range(node.min_rank,child_rank):
                    new_phi = {}
                    for key in phi:
                        new_phi[key] = phi[key]
                    new_phi[node] = i
                    node.phi.append(new_phi)
        elif ch[1].is_leaf(): # right child leaf, left child not leaf
            node.phi = []
            for phi in ch[0].phi:
                child_rank = phi[ch[0]]
                for i in range(node.min_rank,child_rank):
                    new_phi = {}
                    for key in phi:
                        new_phi[key] = phi[key]
                    new_phi[node] = i
                    node.phi.append(new_phi)
        else: # neither child is a leaf
            node.phi = []
            for phi0 in ch[0].phi:
                phi0_vals = set(phi0.values())
                for phi1 in ch[1].phi:
                    phi1_vals = set(phi1.values())
                    if len(phi0_vals.intersection(phi1_vals)) == 0: # no intersection between phi0 and phi1 ranks
                        phi = {}
                        for key in phi0:
                            phi[key] = phi0[key]
                        for key in phi1:
                            phi[key] = phi1[key]
                        max_rank = min(min(phi0_vals),min(phi1_vals))
                        for i in range(node.min_rank,max_rank):
                            new_phi = {}
                            for key in phi:
                                new_phi[key] = phi[key]
                            new_phi[node] = i
                            node.phi.append(new_phi)
    # compute probability
    prob = 0
    for phi in t.seed_node.phi: # for each possible set of rankings,
        for node in phi:          # set each node's label to be its rank
            node.label = phi[node]
        prob += computeProbUnorder(r,t) # probability of the unordered ranked tree
    return prob/(2**sigma)

def symmetric_subtree(node):
    ch = node.child_nodes()
    if len(ch) == 0: # don't want to count leaves
        return False
    if ch[0].is_leaf() and ch[1].is_leaf(): # don't want to count parents of cherries
        return False
    return traverse_subtree(ch[0]) == traverse_subtree(ch[1])

def traverse_subtree(node):
    ch = node.child_nodes()
    if len(ch) == 0:
        return 'U' # U for "UP"
    else:
        left = traverse_subtree(ch[0])
        right = traverse_subtree(ch[1])
        return 'L' + left + 'R' + right + 'U'

def computeProbUnorder(r, t):
    return sum(computeProbOrder(r, t, o) for o in omega(t.internal_nodes()))


def computeProbOrder(r, t, order):
    l=0
    d=1
    nr = 0
    for (i,n) in enumerate(sorted(t.internal_nodes(),key=lambda x: x.label)):
        d *= (r-1)*l+i+1
        if i == 0 or order[n] == 1:
            l+=1
    nr = i+2-l
    return (pow(r,nr-1)/d)

def getOrder(t):
    om = {}
    for (i,n) in enumerate(sorted(t.internal_nodes(),key=lambda x: x.label)):
        om[n] = 1 if n.parent_node and n.parent_node.child_nodes()[1] == n else 0
    return om

def omega(nodes):
    if len(nodes) == 1:
        u = nodes[0]
        ch =  u.child_nodes()
        u12 = [x.is_leaf() for x in ch]
        if u12[0] and u12[1]:
            yield {}
        elif u12[1]:
            yield {ch[0]:0}
            yield {ch[0]:1}
        elif u12[0]:
            yield {ch[1]:0}
            yield {ch[1]:1}
        else:
            yield {ch[0]:0,ch[1]:1}
            yield {ch[0]:1,ch[1]:0}
    else:
        u = nodes[0]
        X = nodes[1:]
        for ox in omega(X):
            for ou in omega([u]):
                out = dict()
                #print (ox, ou)
                out.update(ox)
                out.update(ou)
                yield out

if __name__ == '__main__':
    # parse args
    if len(sys.argv) < 4:
        print("ERROR: Incorrect number of arguments")
        print(USAGE_MESSAGE)
        exit(-1)
    rateA = float(sys.argv[1])
    rateB = float(sys.argv[2])
    trees = dendropy.TreeList.get_from_path(sys.argv[3],schema='newick',suppress_leaf_node_taxa=True)
    treeType = int(sys.argv[4])

    for t in trees:
        if treeType == 0:
            print(str(t)+"; "+str(computeProbOrder(rateA/rateB, t, getOrder(t))))
        elif treeType == 1:
            print(str(t)+"; "+str(computeProbUnorder(rateA/rateB, t)))
        elif treeType == 2:
            print(str(t)+"; "+str(computeProbUnrank(rateA/rateB, t)))
        else:
            print("ERROR: Invalid tree type")
            print(USAGE_MESSAGE)
            exit(-1)
