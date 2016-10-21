#! /usr/bin/env python
'''
Niema Moshiri 2016

Generate plots of fraction of cherries vs. various parameters
'''
# imports
from matplotlib import rcParams
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# settings
sns.set_style("ticks")
rcParams['font.family'] = 'serif'
pal = {'simulated':'#597DBE', 'fasttree':'#76BF72', 'raxml':'#B47CC7', 'theoretical':'#000000'}
handles = [Patch(color=pal['theoretical'],label='Theoretical'),Patch(color=pal['simulated'],label='Simulated')]
axisY = np.asarray([i/10.0 for i in range(0,5)])

# Expected Number of Cherries as a Function of r
def cherries_vs_r(r):
    return (r**0.5)/(1+r+r**0.5)

# DATASETS
# modifying r = lambdaA/lambdaB (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
r_original = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([14,12,7,10,10,12,8,10,8,12,14,7,13,9,8,8,10,9,9,11] +                              # r = 0.0001
                                  [33,28,26,30,25,31,33,28,32,29,28,29,25,27,30,31,32,27,27,27] +                     # r = 0.001
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # r = 0.01
                                  [230,238,226,233,225,219,216,219,225,221,217,224,223,219,222,219,213,225,225,229] + # r = 0.1
                                  [331,326,336,340,348,333,345,326,336,328,319,336,326,327,330,332,335,331,320,329]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying r = lambdaA/lambdaB (with constant lambda = lambdaA + lambdaB)
r2_original = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([12,8,9,9,10,11,11,11,10,10,9,11,11,11,9,9,7,14,11,9] +                             # r = 0.0001
                                  [36,36,36,30,26,25,34,32,31,30,26,30,32,33,33,25,35,29,36,32] +                     # r = 0.001
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # r = 0.01
                                  [220,232,233,225,232,221,221,223,224,230,234,218,230,218,227,227,227,231,223,219] + # r = 0.1
                                  [336,319,341,338,325,323,328,324,327,338,336,330,319,336,333,338,332,334,347,331]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying lambda = lambdaA + lambdaB
l_original = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'cherries':np.array([88,88,91,98,86,90,98,106,96,83,96,83,87,98,98,95,85,96,101,92] +                   # lambda = 33.86550309051126
                                  [97,85,92,87,84,94,96,97,88,93,80,98,95,91,100,91,87,87,90,98] +                    # lambda = 84.66375772627816
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # lambda = 169.32751545255631
                                  [91,89,90,82,94,79,81,89,92,91,90,93,95,92,96,94,91,90,86,94] +                     # lambda = 338.65503090511262
                                  [88,89,89,87,89,87,89,86,85,87,94,84,83,85,84,87,86,84,83,89]                       # lambda = 846.63757726278155
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying sequence length
k_original = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'cherries':np.array([89,94,93,93,96,90,99,96,89,88,87,79,96,96,95,88,81,93,85,91] +                     # length = 50
                                  [93,91,92,91,90,88,100,87,89,89,85,98,87,86,86,88,88,94,91,88] +                    # length = 100
                                  [86,87,84,91,92,87,95,93,82,90,95,91,91,89,84,82,96,85,93,95] +                     # length = 200
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # length = 300
                                  [88,86,88,80,94,91,96,95,91,92,80,91,90,102,84,88,97,90,89,86] +                    # length = 600
                                  [79,94,88,92,88,95,100,94,86,87,84,89,100,90,97,90,87,94,83,91] +                   # length = 1200
                                  [84,93,92,95,91,88,92,93,86,85,95,90,82,84,94,99,86,77,95,95] +                     # length = 2400
                                  [78,92,95,87,94,84,94,88,84,97,86,83,97,87,98,97,85,80,91,80]                       # length = 4800
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying deviation from ultrametricity
g_original = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'cherries':np.array([93,88,91,93,89,80,86,91,84,86,93,92,104,95,88,89,93,84,96,90] +                    # gamma = 2.95181735298926
                                  [85,92,83,89,81,97,94,95,92,96,90,86,81,85,86,87,95,88,88,83] +                     # gamma = 5.90363470597852
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # gamma = 29.518173529892621
                                  [93,85,92,91,90,82,86,85,72,91,89,87,97,78,94,87,91,88,76,87] +                     # gamma = 147.590867649463
                                  [95,86,89,90,84,87,82,92,84,88,89,91,90,95,92,75,91,99,90,95] +                     # gamma = 295.181735298926
                                  [90,86,79,91,83,84,87,89,92,91,97,91,88,96,93,97,89,106,83,86]                      # gamma = infinity
             ).astype(float)/1000} # divide by number of leaves to get percentage

# plot Cherry Fraction vs. r (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r_original),order=x,color=pal['simulated'])
x = np.linspace(-4,0,100)
plt.plot(x+4,cherries_vs_r(10**x),label='Theoretical',linestyle='-',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(E(l_b)=0.298\right)$',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title(r'Cherry Fraction vs. $\log_{10}{r}\ \left(E(l_b)=0.298\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_r_const-exp-branch-length.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Cherry Fraction vs. r (with constant lambda = lambdaA + lambdaB)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r2_original),order=x,color=pal['simulated'])
x = np.linspace(-4,0,100)
plt.plot(x+4,cherries_vs_r(10**x),label='Theoretical',linestyle='-',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(\lambda = \lambda_A + \lambda_B = 169\right)$',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title(r'Cherry Fraction vs. $\log_{10}{r}\ \left(\lambda=\lambda_A+\lambda_B=169\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_r_const-lambda.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Cherry Fraction vs. lambda
fig = plt.figure()
x = np.array([33.866,84.664,169.328,338.655,846.638])
sns.violinplot(x='lambda',y='cherries',data=pd.DataFrame(l_original),order=x,color=pal['simulated'])
x = np.linspace(-100,1000,1100)
plt.plot(x,np.array([cherries_vs_r(0.01)]*len(x)),label='Theoretical',linestyle='-',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\lambda = \lambda_A + \lambda_B$',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title(r'Cherry Fraction vs. $\lambda$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_lambda.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Cherry Fraction vs. length
fig = plt.figure()
x = np.array([50,100,200,300,600,1200,2400,4800])
sns.violinplot(x='length',y='cherries',data=pd.DataFrame(k_original),order=x,color=pal['simulated'])
x = np.linspace(-100,5000,5100)
plt.plot(x,np.array([cherries_vs_r(0.01)]*len(x)),label='Theoretical',linestyle='-',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel('Sequence Length',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title('Cherry Fraction vs. Sequence Length',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_length.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Cherry Fraction vs. gamma rate
fig = plt.figure()
x = np.array([2.952,5.904,29.518,147.591,295.182,float('inf')])
sns.violinplot(x='gammarate',y='cherries',data=pd.DataFrame(g_original),order=x,color=pal['simulated'])
x = np.linspace(-100,1000,5000)
plt.plot(x,np.array([cherries_vs_r(0.01)]*len(x)),label='Theoretical',linestyle='-',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'Gamma Distribution Rate $\left(\alpha\right)$',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title('Cherry Fraction vs. Deviation from Ultrametricity',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_gammarate.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()