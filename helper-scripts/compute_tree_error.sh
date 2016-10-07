#!/bin/bash
# USAGE: Just run this script in the directory containing all of the tree parameter folders

for dir in param*; do
    echo "=== Working on directory $dir ==="
    echo "=== TREE ERROR RF = (FN + FP) / 2 ===" >> $dir/tree_comparison.stats
    for i in $(seq -w 1 20); do
        echo -n "Working on tree $i..."
        echo -n "Tree $i: " >> $dir/tree_comparison.stats
        echo $(echo -n '(' && echo -n `compareTrees.missingBranch $dir/trees_true_simulated/$i.tre $dir/trees_inferred_fasttree/$i.inferred.tre | cut -d' ' -f3` && echo -n ' + ' && echo -n `compareTrees.missingBranch $dir/trees_inferred_fasttree/$i.inferred.tre $dir/trees_true_simulated/$i.tre | cut -d' ' -f3` && echo -n ') / 2') | bc -l >> $dir/tree_comparison.stats
        echo " done"
    done
    echo ""
done
