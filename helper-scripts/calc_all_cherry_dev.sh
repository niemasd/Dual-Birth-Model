#!/bin/bash
for d in $(seq -w 0 24); do
    # do fasttree fixes
    echo -n "param$d" && echo -n "_fasttree = ["
    echo -n `for thresh in $(seq 0 0.01 1.01); do
        for tree in param-$d*/*fasttree*/*.tre; do
            ~/GitHub/Alu-Project/tools/estimate-cherries.sh $tree $thresh 2>/dev/null
        done | ~/GitHub/Alu-Project/helper-scripts/numlist_math.py -avg
    done | ~/GitHub/Alu-Project/helper-scripts/numlist_math.py -csv`
    echo "]"

    # do raxml fixes
	echo -n "param$d" && echo -n "_raxml = ["
    echo -n `for thresh in $(seq 0 0.01 1.01); do
        for tree in param-$d*/*raxml*/*support*.tre; do
            ~/GitHub/Alu-Project/tools/estimate-cherries.sh $tree $thresh 2>/dev/null
        done | ~/GitHub/Alu-Project/helper-scripts/numlist_math.py -avg
    done | ~/GitHub/Alu-Project/helper-scripts/numlist_math.py -csv`
    echo "]"

    # empty line between parameters
    echo ""
done
