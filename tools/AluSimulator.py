'''
Niema Moshiri 2016
Simulate Alu tree
USAGE: python AluSimulator.py <rate> <rate'> <n>
    -rate:  Rate at which active Alus create offspring
    -rate': Rate at which inactive Alus create offspring (become active)
    -n:     Desired total number of leaves in the tree
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
        return self.num == other.num

    # inequality
    def __ne__(self, other):
        return self.num != other.num

    # comparator (for Heap usage)
    def __cmp__(self, other):
        return cmp(self.depth,other.depth)

    # output tree (or subtree) in Newick format
    def newick(self):
        if len(self.children) == 0:
            return str(self.num)
        else:
            lLen = str(self.children[0][0])
            lStr = self.children[0][1].newick()
            rLen = str(self.children[1][0])
            rStr = self.children[1][1].newick()
            return '(' + lStr + ':' + lLen + ',' + rStr + ':' + rLen + ')'

'''
Alu simulation function
INPUT:
    -rate: Rate at which active Alus create offspring
    -rateP: Rate at which inactive Alus create offspring (become active)
    -n:     Desired total number of leaves in the tree
OUTPUT:
    -The simulated tree (as a string in the Newick format)
'''
def simulateAlu(rate, rateP, n):
    # numpy uses scale parameters for exponential (beta = 1/lambda)
    beta = 1/(2*rate)
    betaP = 1/(2*rateP)

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
        print("USAGE: python AluSimulator.py <rate> <rate'> <length>")
        exit(-1)
    rate = float(sys.argv[1])  # lambda
    rateP = float(sys.argv[2]) # lambda'
    n = int(sys.argv[3])       # n

    # perform simulation
    print(simulateAlu(rate,rateP,n))