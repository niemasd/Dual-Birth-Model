#! /usr/bin/env python3
'''
Niema Moshiri 2017

Generate plots of branch length variance.
'''
# imports
from matplotlib import rcParams
from matplotlib.collections import PolyCollection
from matplotlib.patches import Patch
from os.path import realpath
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# settings
LAMBDA = 48.
sns.set_style("ticks")
rcParams['font.family'] = 'serif'
pal = {'var_bl':'#0000FF', 'var_pen_bl':'#00FF00'}

# load data
data_raw = eval(open('/'.join(realpath(__file__).split('/')[:-1]) + '/fig_s2_data.json').read())
data = pd.DataFrame(data_raw)

# branch lengths
handles = [Patch(color=pal['var_bl'],label='Branch Length Variance'), Patch(color=pal['var_pen_bl'],label='Pendant Branch Length Variance')]
fig = plt.figure()
x = np.array(sorted(set(data['r'])))
ax = sns.boxplot(x='r',y='var_bl',data=data,color=pal['var_bl'],width=0.3,showfliers=False)
sns.boxplot(x='r',y='var_pen_bl',data=data,color=pal['var_pen_bl'],width=0.3,showfliers=False)
tick_labels = ax.xaxis.get_ticklabels()
for i in range(len(tick_labels)):
    if x[i] not in {-4.,-3.,-2.,-1.,0.}:
        tick_labels[i].set_visible(False)
x = np.linspace(data_raw['r'][0],data_raw['r'][-1],100)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}$',fontsize=14)
sns.plt.ylabel('Branch Length',fontsize=14)
sns.plt.title(r'Average Pendant and Overall Branch Length vs. $\log_{10}{r}$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('bl-variance_vs_r.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()