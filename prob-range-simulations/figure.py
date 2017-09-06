#! /usr/bin/env python3
# imports
from matplotlib import rcParams
from matplotlib.collections import PolyCollection
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
from sys import argv
import numpy as np
import pandas as pd
import seaborn as sns

# settings
DATA_JSON = '/'.join(argv[0].split('/')[:-1] + ['data_new.json'])
sns.set_style("ticks")
rcParams['font.family'] = 'serif'

# create plot
data = eval(open(DATA_JSON).read())
fig = plt.figure()
ax = sns.pointplot(x='p',y='r',data=data,scale=0.3)
tick_labels = ax.xaxis.get_ticklabels()
for i in range(len(tick_labels)):
    if i % 10 != 0:
        tick_labels[i].set_visible(False)
tick_lines = ax.xaxis.get_ticklines()
for i in range(len(tick_lines)):
    if i % 20 != 0:
        tick_lines[i].set_visible(False)
sns.plt.xlabel(r'$p$',fontsize=14)
sns.plt.ylabel(r'Estimated $\log_{10}{r}$',fontsize=14)
sns.plt.title(r'Estimated $\log_{10}{r}$ vs. $p$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('prob-range-simulations.pdf', format='pdf', bbox_inches='tight')
plt.close()