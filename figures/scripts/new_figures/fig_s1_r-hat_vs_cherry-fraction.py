#! /usr/bin/env python3
'''
Niema Moshiri 2017

Generate plots of inferred r vs. cherry fraction in both normal and log-scale.
'''
# imports
from matplotlib import rcParams
from matplotlib.collections import PolyCollection
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# settings
LAMBDA = 84.
sns.set_style("ticks")
rcParams['font.family'] = 'serif'
pal = {'normal':'#0000FF', 'log':'#00FF00'}

# r as a Function of Cherry Fraction
def r_vs_cherry_fraction(x):
    return (((1-x-((x+1)*(1-3*x))**0.5))/(2*x))**2

# figure
handles = [Patch(color=pal['normal'],label='Normal Scale'),Patch(color=pal['log'],label='Log Scale')]
fig = plt.figure()
ax1 = fig.add_subplot(111)
x = np.linspace(0,1./3.,100)
ax1.plot(x,r_vs_cherry_fraction(x),color=pal['normal'])
sns.plt.ylabel(r'$r$',fontsize=14)
sns.plt.xlabel('Cherry Fraction',fontsize=14)
ax2 = ax1.twinx()
ax2.plot(x,np.log10(r_vs_cherry_fraction(x)),color=pal['log'])
sns.plt.ylabel(r'$\log_{10}{r}$',fontsize=14)
sns.plt.xlabel('Cherry Fraction',fontsize=14)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.title(r'$r$ vs. Cherry Fraction',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('r_vs_cherry-fraction.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()