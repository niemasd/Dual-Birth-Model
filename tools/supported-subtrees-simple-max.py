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
    ht = float(sys.argv[3])
    
    trees = dendropy.TreeList.get_from_path(treeName, 'newick')
    for tree in trees:
        tree.reroot_at_midpoint()
        tree.calc_node_root_distances()
        for node in tree.nodes():
            if node.label is not None:
                node.edge.sp = float(node.label)
            else:
                node.edge.sp = t+2
        filt = lambda edge: False if edge.sp is None or edge.sp >= t or edge.head_node.distance_from_root()>tree.max_distance_from_root()*ht else True
        #print(tree.max_distance_from_root())
        edges = tree.edges(filt)
        for e in edges:
            e.collapse()
        c = 0
        i = 0
        for node in tree.postorder_internal_node_iter():
            if node.num_child_nodes() == len(node.leaf_nodes()):
                c += 1
            i += 1
        print ("%f" %((c+0.0)/len(tree.leaf_nodes())))
        #print (tree.as_string(schema='newick',suppress_leaf_taxon_labels=True,suppress_leaf_node_labels =True,suppress_internal_taxon_labels=True,suppress_internal_node_labels=True,suppress_annotations=True,suppress_edge_lengths=True))
