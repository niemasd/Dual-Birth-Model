#!/bin/bash
# USAGE: Just run this script in the directory containing all of the tree parameter folders

echo "===== COMPUTING CHERRY DEVIATION AS DIFFERENCE (inferred - true) ====="
for dir in param*; do
    echo "=== Working on directory $dir ==="
    for i in $(seq -w 1 20); do
        # fasttree inferred tree
        echo -n "Working on FastTree tree $i..."
        echo -n "Cherry Deviation as Difference (inferred - true): " >> $dir/trees_inferred_fasttree/$i.inferred.fasttree.tre.stats
        echo $(echo -n `cat $dir/trees_inferred_fasttree/$i.inferred.fasttree.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh` && echo -n ' - ' && echo -n `cat $dir/trees_true_simulated/$i.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh`) | bc >> $dir/trees_inferred_fasttree/$i.inferred.fasttree.tre.stats
        echo " done"

        # raxml inferred tree
        echo -n "Working on RAxML tree $i..."
        echo -n "Cherry Deviation as Difference (inferred - true): " >> $dir/trees_inferred_raxml/$i.inferred.raxml.tre.stats
        echo $(echo -n `cat $dir/trees_inferred_raxml/$i.inferred.raxml.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh` && echo -n ' - ' && echo -n `cat $dir/trees_true_simulated/$i.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh`) | bc >> $dir/trees_inferred_raxml/$i.inferred.raxml.tre.stats
        echo " done"

        # true tree (all values should be 0)
        echo -n "Working on true simulated tree $i..."
        echo -n "Cherry Deviation as Difference (inferred - true): " >> $dir/trees_true_simulated/$i.tre.stats
        echo $(echo -n `cat $dir/trees_true_simulated/$i.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh` && echo -n ' - ' && echo -n `cat $dir/trees_true_simulated/$i.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh`) | bc >> $dir/trees_true_simulated/$i.tre.stats
        echo " done"
    done
    echo ""
done

echo "===== COMPUTING CHERRY DEVIATION AS RATIO (inferred / true) ====="
for dir in param*; do
    echo "=== Working on directory $dir ==="
    for i in $(seq -w 1 20); do
        # fasttree inferred tree
        echo -n "Working on FastTree tree $i..."
        echo -n "Cherry Deviation as Ratio (inferred / true): " >> $dir/trees_inferred_fasttree/$i.inferred.fasttree.tre.stats
        echo $(echo -n `cat $dir/trees_inferred_fasttree/$i.inferred.fasttree.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh` && echo -n ' / ' && echo -n `cat $dir/trees_true_simulated/$i.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh`) | bc -l >> $dir/trees_inferred_fasttree/$i.inferred.fasttree.tre.stats
        echo " done"

        # raxml inferred tree
        echo -n "Working on RAxML tree $i..."
        echo -n "Cherry Deviation as Ratio (inferred / true): " >> $dir/trees_inferred_raxml/$i.inferred.raxml.tre.stats
        echo $(echo -n `cat $dir/trees_inferred_raxml/$i.inferred.raxml.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh` && echo -n ' / ' && echo -n `cat $dir/trees_true_simulated/$i.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh`) | bc -l >> $dir/trees_inferred_raxml/$i.inferred.raxml.tre.stats
        echo " done"

        # true tree (all values should be 1)
        echo -n "Working on true simulated tree $i..."
        echo -n "Cherry Deviation as Ratio (inferred / true): " >> $dir/trees_true_simulated/$i.tre.stats
        echo $(echo -n `cat $dir/trees_true_simulated/$i.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh` && echo -n ' / ' && echo -n `cat $dir/trees_true_simulated/$i.tre | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh`) | bc -l >> $dir/trees_true_simulated/$i.tre.stats
        echo " done"
    done
    echo ""
done
