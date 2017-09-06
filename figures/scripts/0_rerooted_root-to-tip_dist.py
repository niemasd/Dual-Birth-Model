#! /usr/bin/env python3
'''
Niema Moshiri 2016

Generate histograms of Alu tree root-to-tip distances after rerooting on best
estimate of 7SLRNA MRCA
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
    print("USAGE: python 0_rerooted_root-to-tip_dist.py <data>")
    exit(-1)
data = eval(open(sys.argv[1]).read())

# create histogram
fig = plt.figure()
sns.distplot(data, hist_kws={'weights':np.ones_like(data)/float(len(data))}, kde=False)
sns.plt.title("Root-to-Tip Distance", fontsize=18, y=1.05)
sns.plt.xlabel("Root-to-Tip Distance", fontsize=14)
sns.plt.ylabel("Frequency", fontsize=14)
sns.plt.show()
fig.savefig(sys.argv[1] + '_rerooted_root-to-tip_dist.pdf', format='pdf', bbox_inches='tight')
plt.close()
