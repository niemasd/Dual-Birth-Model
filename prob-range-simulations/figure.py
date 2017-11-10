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
pal={'true':'#000000','double':'#A9A9A9','ten':'#696969','.05':'#D3D3D3','plot':'#000000'}
#pal={'true':'#000000','double':'#FF0000','ten':'#00FF00','.05':'#FFA500'}

# create plot
data = eval(open(DATA_JSON).read())
fig = plt.figure()
ax = sns.pointplot(x='p',y='r',data=data,scale=0.3,color=pal['plot'])
plt.plot([-10,110],[0.01,0.01],linestyle='--',color=pal['true'])
plt.plot([-10,18],[0.02,0.02],linestyle='--',color=pal['double'])
plt.plot([18,18],[-10,0.02],linestyle='--',color=pal['double'])
plt.plot([-10,50],[0.1,0.1],linestyle='--',color=pal['ten'])
plt.plot([50,50],[-10,0.1],linestyle='--',color=pal['ten'])
plt.plot([-10,5],[0.0115,0.0115],linestyle='--',color=pal['.05'])
plt.plot([5,5],[-10,0.0115],linestyle='--',color=pal['.05'])
ax.set_yscale('log')
tick_labels = ax.xaxis.get_ticklabels()
for i in range(len(tick_labels)):
    if i % 10 != 0:
        tick_labels[i].set_visible(False)
tick_lines = ax.xaxis.get_ticklines()
for i in range(len(tick_lines)):
    if i % 20 != 0:
        tick_lines[i].set_visible(False)
sns.plt.xlabel(r'$p$ (Percent)',fontsize=14)
sns.plt.ylabel(r'Estimated $r$ (log-scale)',fontsize=14)
sns.plt.title(r'Estimated $r$ vs. $p$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('prob-range-simulations.pdf', format='pdf', bbox_inches='tight')
plt.close()
