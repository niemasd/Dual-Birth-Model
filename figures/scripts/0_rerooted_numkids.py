#! /usr/bin/env python
'''
Niema Moshiri 2016

Generate plot  of Alu tree root-to-tip distances after rerooting on best
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
y = sorted([int(i.strip().split(',')[1]) for i in open(sys.argv[1]).read().strip().splitlines()])
x = [i for i in range(len(y))]

# create histogram
fig = plt.figure()
plt.plot(x,y)
plt.plot([-1000,8000],[446,446],linestyle='--',color='#000000')
plt.xlim(0,len(x)+1)
sns.plt.title("Number of 7SLRNA Descendants", fontsize=18, y=1.05)
sns.plt.xlabel(r"Node $u$", fontsize=14)
sns.plt.ylabel(r"Number of 7SLRNA Descendants of Node $u$", fontsize=14)
sns.plt.show()
fig.savefig('0_rerooted_numkids.pdf', format='pdf', bbox_inches='tight')
plt.close()
