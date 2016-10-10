#!/usr/bin/env python

import dendropy
import sys
import os
import copy

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
if __name__ == '__main__':

    if (len(sys.argv) < 3):
        print("USAGE: %s tree_file threshold  " %sys.argv[0])
        sys.exit(1)

    treeName = sys.argv[1]            
    t = float(sys.argv[2])
    
    trees = dendropy.TreeList.get_from_path(treeName, 'newick')
    filt = lambda edge: False if (edge.label is None or (is_number(edge.label) and float(edge.label) >= t)) else True
    for tree in trees:
        for n in tree.internal_nodes():
            if n.label is not None:
                n.label = float (n.label)
                n.edge.label = n.label
        edges = tree.edges(filt)
        for e in edges:
            e.collapse()
        for n in tree.postorder_node_iter():
            if n.is_leaf():
               n.n = 1; n.c = 0;
            elif n.num_child_nodes() == 2 and len(n.leaf_nodes()) == 2:
               n.n = 2; n.c = 1;
            elif n.num_child_nodes() == 2 and (n.child_nodes()[0].is_leaf() or n.child_nodes()[1].is_leaf()):
               n.n = n.child_nodes()[0].n + n.child_nodes()[1].n
               n.c = n.child_nodes()[0].c + n.child_nodes()[1].c
            else:
                n.n = n.c = 0
                nsum = cleaves = 0
                for child in n.child_nodes():
                   n.n += child.n
                   cleaves += 1 if child.is_leaf() else 0
                   if child.c > 0:
                       nsum += child.n
                       n.c  += child.c
                n.c = (n.c+0.0)/nsum*(n.n-cleaves) if nsum > 0 else 0
        print ((tree.seed_node.c+0.0)/tree.seed_node.n)
