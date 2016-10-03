#!/bin/bash
# USAGE: Just run this script in the directory containing all of the tree parameter folders

echo "===== COMPUTING CHERRY DEVIATION AS DIFFERENCE (inferred - true) ====="
for dir in param*; do
    echo "=== Working on directory $dir ==="
    echo "=== CHERRY DEVIATION AS DIFFERENCE (inferred - true) ===" >> $dir/tree_comparison.stats
    for i in $(seq -w 1 20); do
        echo -n "Working on tree $i..."
        echo -n "Tree $i: " >> $dir/tree_comparison.stats
        echo $(echo -n `cat $dir/trees_inferred_fasttree/$i.inferred.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh` && echo -n ' - ' && echo -n `cat $dir/trees_true_simulated/$i.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh`) | bc >> $dir/tree_comparison.stats
        echo " done"
    done
    echo "" >> $dir/tree_comparison.stats
    echo ""
done

echo "===== COMPUTING CHERRY DEVIATION AS RATIO (inferred / true) ====="
for dir in param*; do
    echo "=== Working on directory $dir ==="
    echo "=== CHERRY DEVIATION AS RATIO (inferred / true) ===" >> $dir/tree_comparison.stats
    for i in $(seq -w 1 20); do
        echo -n "Working on tree $i..."
        echo -n "Tree $i: " >> $dir/tree_comparison.stats
        echo $(echo -n `cat $dir/trees_inferred_fasttree/$i.inferred.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh` && echo -n ' / ' && echo -n `cat $dir/trees_true_simulated/$i.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh`) | bc -l >> $dir/tree_comparison.stats
        echo " done"
    done
    echo "" >> $dir/tree_comparison.stats
    echo ""
done
