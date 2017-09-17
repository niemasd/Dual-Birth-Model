#! /usr/bin/env python3
'''
Niema Moshiri 2017

Generate plots of theoretical cherries and average branch length and pendant
branch length with simulated values.
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

def avg(x):
    return float(sum(x))/len(x)

# settings
meancolor = '#FFFFFF'
meansize = 20
LAMBDA = 48.
sns.set_style("ticks")
rcParams['font.family'] = 'serif'
pal = {'cherries':'#FF0000', 'avg_bl':'#0000FF', 'avg_pen_bl':'#00FF00', 'theoretical_cherries':'#FFAAAA', 'theoretical_bl':'#AAAAFF', 'theoretical_pen':'#AAFFAA'}

# Expected Number of Cherries as a Function of r
def cherries_vs_r(r):
    return (r**0.5)/(1+r+r**0.5)

# Expected Average Branch Length as a Function of r
def avg_bl_vs_r(r):
    return ((r+1)/(r**0.5))/(2*LAMBDA)

# Expected Average Pendant Branch Length as a Function of r
def avg_pen_bl_vs_r(r):
    r_fix = np.array([i if i <= 1 else 1./i for i in r])
    return ((r_fix**0.5)/(1+2*(r_fix**0.5)-r_fix))/((LAMBDA*r_fix)/(r_fix+1))

# load data
data_raw = eval(open('/'.join(realpath(__file__).split('/')[:-1]) + '/fig_2_data.json').read())
data = pd.DataFrame(data_raw)

# branch lengths
handles = [Patch(color=pal['theoretical_bl'],label='Theoretical Average Branch Length'), Patch(color=pal['avg_bl'],label='Empirical Average Branch Length'), Patch(color=pal['theoretical_pen'],label='Conjectured Average Pendant Branch Length'), Patch(color=pal['avg_pen_bl'],label='Empirical Average Pendant Branch Length')]
fig = plt.figure()
x = np.array(sorted(set(data['r'])))
ax = sns.boxplot(x='r',y='avg_bl',data=data,color=pal['avg_bl'],width=0.3,showfliers=False)
sns.boxplot(x='r',y='avg_pen_bl',data=data,color=pal['avg_pen_bl'],width=0.3,showfliers=False)
for r in x:
    avg_bl = [data_raw['avg_bl'][i] for i in range(len(data_raw['r'])) if data_raw['r'][i] == r]
    plt.scatter([4*r+16],[avg(avg_bl)],c=meancolor,s=meansize)
    avg_pen_bl = [data_raw['avg_pen_bl'][i] for i in range(len(data_raw['r'])) if data_raw['r'][i] == r]
    plt.scatter([4*r+16],[avg(avg_pen_bl)],c=meancolor,s=meansize)
tick_labels = ax.xaxis.get_ticklabels()
for i in range(len(tick_labels)):
    if x[i] not in {-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.}:
        tick_labels[i].set_visible(False)
x = np.linspace(data_raw['r'][0],data_raw['r'][-1],100)
plt.plot(4*x+16,avg_bl_vs_r(10**x),linestyle='--',color=pal['theoretical_bl'])
plt.plot(4*x+16,avg_pen_bl_vs_r(10**x),linestyle='--',color=pal['theoretical_pen'])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}$',fontsize=14)
sns.plt.ylabel('Branch Length',fontsize=14)
sns.plt.title(r'Average Pendant and Overall Branch Length vs. $\log_{10}{r}$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('theoretical_branch-lengths_vs_r.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# cherry fraction
handles = [Patch(color=pal['theoretical_cherries'],label='Theoretical Cherry Fraction'), Patch(color=pal['cherries'],label='Empirical Cherry Fraction')]
fig = plt.figure()
x = np.array(sorted(set(data['r'])))
ax = sns.boxplot(x='r',y='cherries',data=data,order=x,color=pal['cherries'],width=0.3,showfliers=False)
for r in x:
    cherries = [data_raw['cherries'][i] for i in range(len(data_raw['r'])) if data_raw['r'][i] == r]
    plt.scatter([4*r+16],[avg(cherries)],c=meancolor,s=meansize)
tick_labels = ax.xaxis.get_ticklabels()
for i in range(len(tick_labels)):
    if x[i] not in {-4.,-3.,-2.,-1.,0.,1.,2.,3.,4.}:
        tick_labels[i].set_visible(False)
x = np.linspace(data_raw['r'][0],data_raw['r'][-1],100)
plt.plot(4*x+16,cherries_vs_r(10**x),linestyle='--',color=pal['theoretical_cherries'])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}$',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title(r'Cherry Fraction vs. $\log_{10}{r}$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('theoretical_cherry-fraction_vs_r.pdf', format='pdf', bbox_inches='tight')
plt.close()