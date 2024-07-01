This is the Git repository containing all code and simulation data for the paper titled "A two-state model of tree evolution and its applications to *Alu* retrotransposition" ([doi:10.1093/sysbio/syx088](https://doi.org/10.1093/sysbio/syx088)). The supplementary files for the paper can be found [here](https://doi.org/10.5061/dryad.13n52).

**NOTE:** If you want to sample trees under the dual-birth, **DO NOT** use the simulator in this repository! The original algorithm proposed in the paper is O(*n* log *n*) for a tree with *n* leaves, but we more recently proposed a O(*n*) algorithm that we proved correct and implemented in C++ ("A linear-time algorithm to sample the dual-birth model", [doi:10.1101/226423](https://doi.org/10.1101/226423)), which can be found [here](https://github.com/niemasd/Dual-Birth-Simulator). The original implementation is being kept here for the sake of reproducibility of the original paper.

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
* **[helper-scripts](helper-scripts):** Small scripts that helped automate various tasks
