#!/bin/bash
# WARNING: This script needs numlist, which is a program located in my "tools" GitHub repo
# USAGE: Just run this script in the directory containing all of the tree parameter folders

command -v numlist >/dev/null 2>&1 || { echo >&2 "ERROR: numlist not found in PATH. Get numlist from my \"tools\" GitHub repo (niemasd/tools)."; exit 1; }

# using estimate-cherries.sh
echo "y_estimate_cherries_sh = {"
echo "    # fasttree values"
for d in $(seq -w 0 24); do
    # do fasttree fixes (fasttree support values are decimals, so do 0-1)
    echo -n "    'param$d" && echo -n "_fasttree':["
    echo -n `for thresh in $(seq 0 0.01 1.01); do
        for tree in param-$d*/*fasttree*/*.tre; do
            ~/GitHub/Alu-Project/tools/estimate-cherries.sh $tree $thresh 2>/dev/null
        done | numlist -avg
    done | numlist -csv`
    echo "],"
done
echo ""
echo "    # RAxML values"
for d in $(seq -w 0 24); do
    # do raxml fixes (raxml support values are percentages, so do 0-100)
    echo -n "    'param$d" && echo -n "_raxml':["
    echo -n `for thresh in $(seq 0 100); do
        for tree in param-$d*/*raxml*/*support*.tre; do
            ~/GitHub/Alu-Project/tools/estimate-cherries.sh $tree $thresh 2>/dev/null
        done | numlist -avg
    done | numlist -csv`
    echo "],"
done
echo "}"
echo ""

# using supported-subtrees-min.py
echo "y_supported_subtrees_min_py = {"
echo "    # fasttree values"
for d in $(seq -w 0 24); do
    # do fasttree fixes (fasttree support values are decimals, so do 0-1)
    echo -n "    'param$d" && echo -n "_fasttree':["
    echo -n `for thresh in $(seq 0 0.01 1.01); do
        for tree in param-$d*/*fasttree*/*.tre; do
            ~/GitHub/Alu-Project/tools/supported-subtrees-min.py $tree $thresh  2>/dev/null
        done | numlist -avg
    done | numlist -csv`
    echo "],"
done
echo ""
echo "    # RAxML values"
for d in $(seq -w 0 24); do
    # do raxml fixes (raxml support values are percentages, so do 0-100)
    echo -n "    'param$d" && echo -n "_raxml':["
    echo -n `for thresh in $(seq 0 100); do
        for tree in param-$d*/*raxml*/*support*.tre; do
            ~/GitHub/Alu-Project/tools/supported-subtrees-min.py $tree $thresh 2>/dev/null
        done | numlist -avg
    done | numlist -csv`
    echo "],"
done
echo "}"

# using supported-subtrees-simple.py
echo "y_supported_subtrees_simple_py = {"
echo "    # fasttree values"
for d in $(seq -w 0 24); do
    # do fasttree fixes (fasttree support values are decimals, so do 0-1)
    echo -n "    'param$d" && echo -n "_fasttree':["
    echo -n `for thresh in $(seq 0 0.01 1.01); do
        for tree in param-$d*/*fasttree*/*.tre; do
            ~/GitHub/Alu-Project/tools/supported-subtrees-simple.py $tree $thresh  2>/dev/null
        done | numlist -avg
    done | numlist -csv`
    echo "],"
done
echo ""
echo "    # RAxML values"
for d in $(seq -w 0 24); do
    # do raxml fixes (raxml support values are percentages, so do 0-100)
    echo -n "    'param$d" && echo -n "_raxml':["
    echo -n `for thresh in $(seq 0 100); do
        for tree in param-$d*/*raxml*/*support*.tre; do
            ~/GitHub/Alu-Project/tools/supported-subtrees-simple.py $tree $thresh 2>/dev/null
        done | numlist -avg
    done | numlist -csv`
    echo "],"
done
echo "}"