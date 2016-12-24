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
            print(str(t)+";",computeProbOrder(rateA/rateB, t, getOrder(t)))
        elif treeType == 1:
            print(str(t)+";",sum(computeProbOrder(rateA/rateB, t, o) for o in omega(t.internal_nodes())))
        elif treeType == 2:
            print("DO UNRANKED UNORDERED PROBABILITY")
        else:
            print("ERROR: Invalid tree type")
            print(USAGE_MESSAGE)
            exit(-1)
