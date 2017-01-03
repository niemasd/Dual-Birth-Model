#!/bin/bash

rep=100000;
la=$1;
lb=$2;

# ORIGINAL (ordered ranked and unordered ranked)
#python DualBirthSimulator.py $la $lb 6 $rep|nw_topology -L -|sed -e "s/I//g" -e "s/,)/,d)/g" -e "s/(,/(d,/g" |tee >(sort|uniq -c|sort -k2 > dis_${la}_${lb}_${rep}) | (nw_order -|sort|uniq -c|sort -k2 > unorddis_${la}_${lb}_${rep})

# NIEMA'S (ordered ranked, unordered ranked, and unordered unranked)
python DualBirthSimulator.py $la $lb 6 $rep|nw_topology -L -|sed -e "s/I//g" -e "s/,)/,d)/g" -e "s/(,/(d,/g" |tee >(sort|uniq -c|sort -k2 > dis_${la}_${lb}_${rep}) |tee >(nw_order -|sort|uniq -c|sort -k2 > unorddis_${la}_${lb}_${rep}) | (sed -e "s/[0-9]//g" | nw_order -cn - | sort | uniq -c | sort -k2 > unrankdis_${la}_${lb}_${rep})

join -11 -22  <(python ComputeProb.py $la $lb <(sed -e "s/.* //g" dis_${la}_${lb}_${rep}) 0) <(cat dis_${la}_${lb}_${rep})|sort -k2n|tee dist_${la}_${lb}_${rep}.stat

join -11 -22  <(python ComputeProb.py $la $lb <(sed -e "s/.* //g" unorddis_${la}_${lb}_${rep}) 1) <(cat unorddis_${la}_${lb}_${rep})|sort -k2n|tee unorddist_${la}_${lb}_${rep}.stat

join -11 -22  <(python ComputeProb.py $la $lb <(sed -e "s/.* //g" unrankdis_${la}_${lb}_${rep}) 2) <(cat unrankdis_${la}_${lb}_${rep})|sort -k2n|tee unrankdist_${la}_${lb}_${rep}.stat
