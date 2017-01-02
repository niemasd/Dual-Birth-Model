#!/bin/bash

# USAGE: generate-trees.sh <rateA> <rateB> <num_leaves> <num_trees>

for i in $(seq -w 1 $4); do
    echo "Generating tree $i...";
    ~/GitHub/Alu-Project/tools/DualBirthSimulator.py $1 $2 $3 > $i.tre.ULTRAMETRIC;
done
