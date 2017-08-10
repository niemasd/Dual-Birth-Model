#! /usr/bin/env python
'''
Niema Moshiri 2016

Simulate Alu tree

See Theorem 3.3 from Stadler & Steel (2012) for proof about branch lengths
'''

# imports
import sys
import argparse
from random import random
from numpy.random import exponential
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
sys.setrecursionlimit(1000000000)
VERBOSE = False

# define Node class
class Node:
    numNodes = 0 # total number of Node objects, used to make Node IDs

    # constructor
    def __init__(self, depth, parent=None):
        self.parent = parent     # Node's parent (None if root)
        self.depth = depth       # Node's depth (0 if root)
        self.children = []       # Node's children, (branchlength,Node) tuples
        self.num = Node.numNodes # Node's identifier
        self.label= None
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

    def __lt__(self, other):
        return self.depth < other.depth

    # output tree (or subtree) in Newick format
    def newick(self):
        # if leaf
        if len(self.children) == 0:
            return "L" + str(self.num)

        # if internal node
        else:
            lLen = str(self.children[0][0])
            lStr = self.children[0][1].newick()
            rLen = str(self.children[1][0])
            rStr = self.children[1][1].newick()
            out = '(' + lStr + ':' + lLen + ',' + rStr + ':' + rLen + ')I' + str(self.label)
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
def simulateAlu(rateA, rateB, n, p):
    # numpy uses scale parameters for exponential (beta = 1/lambda)
    beta = 1/(float(rateB))
    betaP = 1/(float(rateA))

    # initialize simulation
    root = Node(depth=0, parent=None)
    root.right = True # True = right child, False = left child
    pq = Q.PriorityQueue()
    pq.put(root) # priority queue is MinHeap on node depth

    # perform simulation
    numInternal = 0
    while pq.qsize() < n:
        # pop off of priority queue
        currNode = pq.get()
        currNode.label = numInternal
        numInternal+=1

        # self propagation
        leftLength = exponential(scale={True:beta,False:betaP}[random()<p])
        leftChild = Node(depth=currNode.depth+leftLength, parent=currNode)
        leftChild.right = False

        # newly created inactive child
        rightLength = exponential(scale=beta)
        rightChild = Node(depth=currNode.depth+rightLength, parent=currNode)
        rightChild.right = True

        # add new children to parent's "children" list, and add them to pq
        currNode.children = [(leftLength,leftChild),(rightLength,rightChild)]
        pq.put(leftChild)
        pq.put(rightChild)
        #print >>sys.stderr, (leftLength, rightLength)

    # get leaves from pq
    leaves = []
    counts = {True:0,False:0} # True = right, False = left
    while not pq.empty():
        leaf = pq.get()
        leaves.append(leaf)
        counts[leaf.right] += 1
        if VERBOSE:
            if leaf.right:
                sys.stderr.write("Uncensored Right Pendant Edge Length: %f\n" % (leaf.depth - leaf.parent.depth))
            else:
                sys.stderr.write("Uncensored Left Pendant Edge Length: %f\n" % (leaf.depth - leaf.parent.depth))
    if VERBOSE:
        sys.stderr.write("Number of Right Leaves: %d\n" % counts[True])
        sys.stderr.write("Number of Left Leaves: %d\n" % counts[False])
        sys.stderr.write("Number of Right Internals: %d\n" % (n - 1  - counts[True]))
        sys.stderr.write("Number of Left Internals: %d\n" % (n - 1 - counts[False]))

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
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-la', '--lambdaA', required=True, type=float, help="Activation Rate (lambda A)")
    parser.add_argument('-lb', '--lambdaB', required=True, type=float, help="Birth Rate (lambda B)")
    parser.add_argument('-n', '--leaves', required=True, type=int, help="Number of Leaves")
    parser.add_argument('-r', '--replicates', required=False, type=int, default=1, help="Number of Replicates")
    parser.add_argument('-p', '--prob', required=False, type=float, default=0., help="Probability that Both Children are Active")
    parser.add_argument('-v', '--verbose', action="store_true", help="Verbose Mode")
    args = parser.parse_args()
    assert args.prob >= 0 and args.prob <= 1, "Probability must be between 0 and 1"
    VERBOSE = args.verbose

    # perform simulation
    for i in range(0,args.replicates):
        print(simulateAlu(args.lambdaA,args.lambdaB,args.leaves,args.prob))
