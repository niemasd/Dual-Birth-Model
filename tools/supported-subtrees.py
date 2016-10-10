#!/usr/bin/env python
'''
Created on Jun 3, 2011

@author: smirarab
'''
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

    if (len(sys.argv) < 2):
        print("USAGE: %s tree_file [threshold - default 75] [outfile name; - uses default] [-strip-internal|-strip-bl|strip-both|-nostrip; default: nostrip]" %sys.argv[0])
        sys.exit(1)

    treeName = sys.argv[1]            
    t = 75 if len (sys.argv) < 3 else float(sys.argv[2])
    resultsFile="%s.%d" % (treeName,t * 100 if t < 1 else t) if len (sys.argv) < 4 or sys.argv[3]=="-" else sys.argv[3]
    #print "outputting to", resultsFile    
    strip_internal=True if len (sys.argv) > 4 and ( sys.argv[4]=="-strip-internal" or sys.argv[4]=="-strip-both" ) else False 
    strip_bl=True if len (sys.argv) > 4 and ( sys.argv[4]=="-strip-bl" or sys.argv[4]=="-strip-both" ) else False
    
    trees = dendropy.TreeList.get_from_path(treeName, 'newick')
    filt = lambda edge: False if (edge.label is None or (is_number(edge.label) and float(edge.label) >= t)) else True
    outtrees = dendropy.TreeList()
    for tree in trees:
        for n in tree.internal_nodes():
            if n.label is not None:
                n.label = float (n.label)
                n.edge.label = n.label
                #print n.label
                #n.label = round(n.label/2)   
        edges = tree.edges(filt)
        #print(len(edges), "edges will be removed", file=sys.stderr)
        for e in edges:
            e.collapse()
        if strip_internal:
            for n in tree.internal_nodes():
                n.label = None
        if strip_bl:
            for e in tree.get_edge_set():
                e.length = None
        for n in tree.postorder_node_iter():
            if n.is_leaf():
               n.n = 1; n.c = 0;
            elif n.num_child_nodes() == 2 and len(n.leaf_nodes()) == 2:
               n.n = 2; n.c = 1;
            elif n.num_child_nodes() == 2 and (n.child_nodes()[0].is_leaf() or n.child_nodes()[1].is_leaf()):
               n.n = n.child_nodes()[0].n+n.child_nodes()[1].n
               n.c = n.child_nodes()[0].c+n.child_nodes()[1].c
            else:
                #print ("polytomy size: %d" %n.num_child_nodes())
                #print (n.as_string(schema='newick'))
                n.n = n.c = 0
                nsum = cleaves = 0
                for child in n.child_nodes():
                   n.n += child.n
                   cleaves += 1 if child.is_leaf() else 0
                   if child.c > 0:
                       nsum += child.n
                       n.c  += child.c
                n.c = (n.c+0.0)/nsum*(n.n-cleaves) if nsum > 0 else 0
                #print ("%d %d" %(n.c,n.n) )
        print ((tree.seed_node.c+0.0)/tree.seed_node.n)
        #print(p.as_string(schema='newick'))

        #tree.reroot_at_midpoint(update_splits=False)
        
    outtrees.write(file=open(resultsFile,'w'),schema='newick')
