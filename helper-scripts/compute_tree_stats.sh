#!/bin/bash
# WARNING: This script needs numlist, which is a program located in my "tools" GitHub repo

# compute tree stats on all trees in the current working directory (*.tre.gz files)
# so far, only does fast stats:
#    - Number of Cherries
#    - Average Branch Length
# does NOT do slower stats:
#    - RAxML GAMMA-based Score
for tree in *.tre.gz; do
    # get tre file prefix (*.tre from *.tre.gz)
    treFile=${tree%.*}

    # compute number of cherries
    echo -n "Number of Cherries: " >> $treFile.stats
    gunzip -c $tree | ~/GitHub/Alu-Project/helper-scripts/count_cherries.sh >> $treFile.stats

    # compute average branch length
    echo -n "Average Branch Length: " >> $treFile.stats
    gunzip -c $tree | nw_distance -mp -sa - | ~/GitHub/Alu-Project/helper-scripts/numlist -avg >> $treFile.stats
done
