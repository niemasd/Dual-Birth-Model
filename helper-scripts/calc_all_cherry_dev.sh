#!/bin/bash
# USAGE: Just run this script in the directory containing all of the tree parameter folders
for d in $(seq -w 0 24); do
    # do fasttree fixes (fasttree support values are decimals, so do 0-1)
    echo -n "param$d" && echo -n "_fasttree = ["
    echo -n `for thresh in $(seq 0 0.01 1.01); do
        for tree in param-$d*/*fasttree*/*.tre; do
            ~/GitHub/Alu-Project/tools/estimate-cherries.sh $tree $thresh 2>/dev/null
        done | ~/GitHub/Alu-Project/helper-scripts/numlist_math.py -avg
    done | ~/GitHub/Alu-Project/helper-scripts/numlist_math.py -csv`
    echo "]"

    # do raxml fixes (raxml support values are percentages, so do 0-100)
	echo -n "param$d" && echo -n "_raxml = ["
    echo -n `for thresh in $(seq 0 100); do
        for tree in param-$d*/*raxml*/*support*.tre; do
            ~/GitHub/Alu-Project/tools/estimate-cherries.sh $tree $thresh 2>/dev/null
        done | ~/GitHub/Alu-Project/helper-scripts/numlist_math.py -avg
    done | ~/GitHub/Alu-Project/helper-scripts/numlist_math.py -csv`
    echo "]"

    # empty line between parameters
    echo ""
done
