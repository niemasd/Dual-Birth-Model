#! /usr/bin/env python
'''
Niema Moshiri 2016
Simulate Alu tree

See Theorem 3.3 from Stadler & Steel (2012) for proof about branch lengths

USAGE: python AluSimulator.py <rateA> <rateB> <n>
    -rateA: (A)ctivation Rate, rate at which inactive Alus create offspring
    -rateB: (B)irth Rate, rate at which active Alus create offspring
    -n:     Desired total number of leaves in the tree

Biologically, it makes sense to have rateB >> rateA
'''
# imports
import sys
from numpy.random import exponential
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

# define Node class
class Node:
    numNodes = 0 # total number of Node objects, used to make Node IDs

    # constructor
    def __init__(self, depth, parent=None):
        self.parent = parent     # Node's parent (None if root)
        self.depth = depth       # Node's depth (0 if root)
        self.children = []       # Node's children, (branchlength,Node) tuples
        self.num = Node.numNodes # Node's identifier
        Node.numNodes += 1

    # equality
    def __eq__(self, other):
        if other is None:
            return self is None
        return self.num == other.num

    # inequality
    def __ne__(self, other):
        return self.num != other.num

    # comparator (for Heap usage)
    def __cmp__(self, other):
        return cmp(self.depth,other.depth)

    # output tree (or subtree) in Newick format
    def newick(self):
        # if leaf
        if len(self.children) == 0:
            return str(self.num)

        # if internal node
        else:
            lLen = str(self.children[0][0])
            lStr = self.children[0][1].newick()
            rLen = str(self.children[1][0])
            rStr = self.children[1][1].newick()
            out = '(' + lStr + ':' + lLen + ',' + rStr + ':' + rLen + ')'
            if self.parent == None: # if root, need semicolon (entire tree)
                out += ';'
            return out

'''
Alu simulation function
INPUT:
    -rate: Rate at which active Alus create offspring
    -rateP: Rate at which inactive Alus create offspring (become active)
    -n:     Desired total number of leaves in the tree
OUTPUT:
    -The simulated tree (as a string in the Newick format)
'''
def simulateAlu(rateA, rateB, n):
    # numpy uses scale parameters for exponential (beta = 1/lambda)
    beta = 1/(float(rateB))
    betaP = 1/(float(rateA))

    # initialize simulation
    root = Node(depth=0, parent=None)
    pq = Q.PriorityQueue()
    pq.put(root) # priority queue is MinHeap on node depth

    # perform simulation
    while pq.qsize() < n:
        # pop off of priority queue
        currNode = pq.get()

        # self propogation
        leftLength = exponential(scale=beta)
        leftChild = Node(depth=currNode.depth+leftLength, parent=currNode)

        # newly created inactive child
        rightLength = exponential(scale=betaP)
        rightChild = Node(depth=currNode.depth+rightLength, parent=currNode)

        # add new children to parent's "children" list, and add them to pq
        currNode.children = [(leftLength,leftChild),(rightLength,rightChild)]
        pq.put(leftChild)
        pq.put(rightChild)
        #print >>sys.stderr, (leftLength, rightLength)

    # get leaves from pq
    leaves = []
    while not pq.empty():
        leaves.append(pq.get())

    # truncate final edges to be same as shortest leaf
    minDepth = leaves[0].depth
    for leaf in leaves:
        leaf.depth = minDepth
        if leaf.parent.children[0][1] == leaf:
            leaf.parent.children[0] = (minDepth - leaf.parent.depth, leaf)
        else:
            leaf.parent.children[1] = (minDepth - leaf.parent.depth, leaf)

    # return tree in Newick format
    return root.newick()

# if code is executed (and not imported)
if __name__ == '__main__':
    # parse args
    if len(sys.argv) != 4:
        print("ERROR: Incorrect number of arguments")
        print("USAGE: python AluSimulator.py <rateA> <rateB> <n>")
        exit(-1)
    rateA = float(sys.argv[1])
    rateB = float(sys.argv[2])
    n = int(sys.argv[3])

    # perform simulation
    print(simulateAlu(rateA,rateB,n))
