DESCRIPTIONS
===
* [break_ultrametricity.py](tools/break_ultrametricity.py): Resize all branches in a tree by sampling from gamma distribution with expected value 1 (to keep expected branch length constant)
* [calc_all_cherry_dev.sh](helper-scripts/calc_all_cherry_dev.sh): Compute cherry deviations of inferred trees after Cherry Estimate Correction
* [compute-distributions.sh](helper-scripts/compute-distributions.sh): Empirically compute probability distributions of tree shape
* [compute_avg_tip-to-tip_dist.sh](helper-scripts/compute_avg_tip-to-tip_dist.sh): Compute average tip-to-tip distance
* [compute_tree_cherry_deviation.sh](helper-scripts/compute_tree_cherry_deviation.sh): Compute cherry deviations of inferred trees before Cherry Estimate Correction
* [compute_tree_error.sh](helper-scripts/compute_tree_error.sh): Compute tree error using various metrics
* [compute_tree_stats.sh](helper-scripts/compute_tree_stats.sh): Compute number of cherries (uncorrected) and average branch length for all trees
* [count_cherries.sh](helper-scripts/count_cherries.sh): Count the number of cherries in a tree
* [generate_indelible_control.py](helper-scripts/generate_indelible_control.py): Generate an INDELible control file
* [generate_trees.sh](helper-scripts/generate_trees.sh): Generate multiple trees using our simulator ([AluSimulator.py](tools/AluSimulator.py))
* [plot_cherries-vs-rateA.py](helper-scripts/plot_cherries-vs-rateA.py): Generate many trees using our simulator and plot the number of cherries vs. λa
* [run_cherries.sh](helper-scripts/run_cherries.sh): Generate many trees using our simulator and plot the number of cherries vs. r
