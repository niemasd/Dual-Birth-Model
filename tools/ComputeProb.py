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
USAGE: python ComputeProb.py <rateA> <rateB> <tree> <0 for ordered or 1 for unordered>
    -rateA: (A)ctivation Rate, rate at which inactive Alus create offspring
    -rateB: (B)irth Rate, rate at which active Alus create offspring
    -tree:  A file with trees to be scored

Biologically, it makes sense to have rateB >> rateA
'''

def computeProb(r,t):
    l=0
    d=1
    nr = 0
    for (i,n) in enumerate(sorted(t.internal_nodes(),key=lambda x: x.label)):
        #print (l,)
        d *= (r-1)*l+i+1
        if n.parent_node is None or n.parent_node.child_nodes()[1] == n:
            l+=1
    nr = i+2-l
    return (pow(r,nr-1)/d)

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

def w(order,ranks,i):
    return order[ranks[i]]

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
    if len(sys.argv) < 3:
        print("ERROR: Incorrect number of arguments")
        print(USAGE_MESSAGE)
        exit(-1)
    rateA = float(sys.argv[1])
    rateB = float(sys.argv[2])
    trees = dendropy.TreeList.get_from_path(sys.argv[3],schema='newick',suppress_leaf_node_taxa=True)
    ord = True if int(sys.argv[4]) == 1 else False

    for t in trees:
        if ord:
            ranks = sorted(t.internal_nodes(),key=lambda x: x.label)
            # print("\n".join(str(o) for o in omega(t.internal_nodes()))) 
            print(str(t)+";",sum(computeProbOrder(rateA/rateB, t, o) for o in omega(t.internal_nodes()))) 
        else:
            print(str(t)+";",computeProb(rateA/rateB,t))

