This is the Git repository containing all code and simulation data for the paper titled "A two-state model of tree evolution and its applications to *Alu* retrotransposition."

REQUIREMENTS
===
* **Python Modules**
    * [DendroPy](http://www.dendropy.org/)
    * [matplotlib](http://matplotlib.org/)
    * [NumPy](http://www.numpy.org/)
    * [SciPy](https://www.scipy.org/)
    * [Seaborn](http://seaborn.pydata.org/)
* **Software**
    * My [tools](https://github.com/niemasd/tools/) repository (numlist, specifically)
    * [FastTree](http://www.microbesonline.org/fasttree/)
    * [INDELible](http://abacus.gene.ucl.ac.uk/software/indelible/)
    * [RAxML](http://sco.h-its.org/exelixis/web/software/raxml/index.html)

DESCRIPTIONS
===
* **[tools](tools):** The tools we developed in this paper
    * [AluSimulator.py](tools/AluSimulator.py): Our implementation of the Dual-Birth generative process
    * [estimate-cherries.sh](tools/estimate-cherries.sh): The Cherry Estimate Correction method we used in our paper
    * [supported-subtrees-min.py](tools/supported-subtrees-min.py): Alternative Cherry Estimate Correction method (unused)
    * [supported-subtrees-simple-max.py](tools/supported-subtrees-simple-max.py): Alternative Cherry Estimate Correction method (unused)
    * [supported-subtrees-simple.py](tools/supported-subtrees-simple.py): Alternative Cherry Estimate Correction method (unused)
    * [supported-subtrees.py](tools/supported-subtrees.py): Alternative Cherry Estimate Correction method (unused)
<br/><br/>
* **[helper-scripts](helper-scripts)**: Small scripts that helped automate various tasks
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
    
