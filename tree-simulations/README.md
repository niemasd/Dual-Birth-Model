# Tree Simulations #
Each folder corresponds to a single set of parameters (the exact parameters are listed in each folder's README file). True trees were generated using our simulation tool ([AluSimulator.py](tools/AluSimulator.py)). Then, sequence alignments were generated for each tree using INDELible using the parameters listed below. Then, trees were inferred from these alignments using both FastTree-II and RAxML (the exact commands used can be found in the supplement of our paper). SH-like branch support values were then computed on the RAxML-inferred trees using RAxML (again, see supplement for exact commands).

### Global Parameters (Alignment Simulation) ###
* GTR Frequencies: 0.2922 0.2319 0.2401 0.2358
* GTR rates(ac ag at cg ct gt) 0.8896 2.9860 0.8858 1.0657 3.8775 1.0000
* alpha = 5.256
