#! /usr/bin/env python3
'''
Niema Moshiri 2016

Generate histograms of Alu sequence bitscore (from unfiltered DfamScan FASTA)
'''
# imports
from matplotlib import rcParams
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sys

# settings
sns.set_style("ticks")
rcParams['font.family'] = 'serif'
if len(sys.argv) < 2:
    print("ERROR: Incorrect number of arguments")
    print("USAGE: python 0_tree_support_histogram.py <CSV_of_branch_support>")
    exit(-1)
data = [float(i) for i in open(sys.argv[1]).read().strip().split(',')]

# create histogram
fig = plt.figure()
sns.distplot(data, hist_kws={'weights':np.ones_like(data)/float(len(data))}, kde=False)
sns.plt.title("Branch Support", fontsize=18, y=1.05)
sns.plt.xlabel("Branch Support", fontsize=14)
sns.plt.ylabel("Frequency", fontsize=14)
sns.plt.show()
fig.savefig(sys.argv[1] + '_support.pdf', format='pdf', bbox_inches='tight')
plt.close()
