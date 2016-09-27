#! /usr/bin/env python
'''
Niema Moshiri 2016

For each branch in the input tree, sample a multiplier from a Gamma distribution
defined by the given parameter alpha = beta such that the expected branch length
remains the same after resizing.

USAGE: python break-ultrametricity.py <gamma_param> <tree_file>
    -gamma_param: alpha = beta parameter for Gamma distribution
    -tree_file:   path to the tree (in Newick format), or - to specify STDIN
'''
# imports
import dendropy
import sys
from scipy.stats import gamma

# perform resizing of tree branches
def resizeBranches(param, tree):
    edges = tree.edges()
    multipliers = gamma.rvs(param, scale=1/param, size=len(edges))
    for i in range(len(edges)):
        edge = edges[i]
        if edge.length != None:
            edge.length = edge.length * multipliers[i]

# if code is executed (and not imported)
if __name__ == '__main__':
    # parse args
    if len(sys.argv) != 3:
        print("ERROR: Incorrect number of arguments")
        print("USAGE: python break-ultrametricity.py <gamma_param> <tree_file>")
        print("    -gamma_param: alpha = beta parameter for Gamma distribution")
        print("    -tree_file:   path to the tree (in Newick format), or - to specify STDIN")
        print()
        exit(-1)
    param = float(sys.argv[1])
    if sys.argv[2].strip() == '-':
        tree = dendropy.Tree.get_from_string(sys.stdin.read().strip(),'newick')
    else:
        tree = dendropy.Tree.get_from_string(open(sys.argv[2]).read().strip(),'newick')

    # perform branch resizing
    resizeBranches(param,tree)

    # print resulting tree
    print(tree.as_string(schema='newick'))