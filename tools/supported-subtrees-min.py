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
    filt = lambda edge: False if (edge.sp is None or (is_number(edge.sp) and float(edge.sp) >= t)) else True
    for tree in trees:
        for node in tree.nodes():
            if node.label is not None:
                node.edge.sp = float(node.label)
            else:
                node.edge.sp = 10000
        edges = tree.edges(filt)
        for e in edges:
            e.collapse()
        for node in tree.postorder_node_iter():
            if node.is_leaf():
               node.n = 1; node.c = 0; node.m = 0;
            elif node.num_child_nodes() == 2 and len(node.leaf_nodes()) == 2:
               node.n = 2; node.c = 1; node.m = 1;
            elif node.num_child_nodes() == 2 and (node.child_nodes()[0].is_leaf() or node.child_nodes()[1].is_leaf()):
               node.n = node.child_nodes()[0].n + node.child_nodes()[1].n
               node.c = node.child_nodes()[0].c + node.child_nodes()[1].c
               node.m = node.child_nodes()[0].m + node.child_nodes()[1].m
            else:
                node.n = node.c = node.m = 0
                for child in node.child_nodes():
                   if child.c > 0:
                       node.n += child.n
                       node.c += child.c
                   node.m += child.m
                ext = -1 if node.n == 0 else (node.c+0.0)/node.n 
                ss = node.n
                for child in node.child_nodes():
                    if child.c == 0:
                        node.n += child.n
                        node.c += 0 if ext == -1 or child.n == 1  else max(ext*child.n,child.m)
                        #node.m += max(ext*child.n,child.m)
                node.m = max (node.m, 1)
                #node.c = (node.c+0.0)/nsum*(node.n-cleaves) if nsum > 0 else 0
            #if node.c != node.m:
            #    print("%d %d %d %s" %(node.n,node.c,node.m,node._as_newick_string(suppress_leaf_taxon_labels=True,suppress_leaf_node_labels =True,suppress_internal_taxon_labels=True,suppress_internal_node_labels=True,suppress_annotations=True,suppress_edge_lengths=True)))
        print ((tree.seed_node.c+0.0)/tree.seed_node.n)
