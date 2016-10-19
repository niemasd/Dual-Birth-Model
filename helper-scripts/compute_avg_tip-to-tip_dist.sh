#!/bin/bash
# WARNING: This script needs numlist, which is a program located in my "tools" GitHub repo
# USAGE: ./compute_avg_tip-to-tip_dist.sh <true_tree_file> <inferred_tree_file> <num_iterations>
# Note that we hardcode 1000 leaves below

command -v numlist >/dev/null 2>&1 || { echo >&2 "ERROR: numlist not found in PATH. Get numlist from my \"tools\" GitHub repo (niemasd/tools)."; exit 1; }

for x in {1..$2}; do r=$((RANDOM % 1000 + 1)); paste <(nw_reroot $0 $r | nw_distance -mr -sf -) <(nw_reroot $1 $r|nw_distance -mr -sf -)  |awk '{print sqrt(($1-$2)^2)}'|numlist -avg; done 2>/dev/null |numlist -avg
