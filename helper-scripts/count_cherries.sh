#!/bin/bash
# count cherries in tree (Newick format) passed in via STDIN
echo "$(cat)" | grep -o -E '\([^(),]+\,[^(),]+\)' | wc -l | tr -d '[[:space:]]' && echo
