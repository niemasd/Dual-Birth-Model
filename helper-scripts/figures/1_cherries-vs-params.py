#! /usr/bin/env python
'''
Niema Moshiri 2016

Generate plots of number of cherries vs. rateA (activation rate)
'''
# imports
from matplotlib import rcParams
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# settings
rcParams['font.family'] = 'serif'

# Expected Number of Cherries as a Function of r
def cherries_vs_r(r):
    return (r**0.5)/(1+r+r**0.5)

# DATASETS
# modifying r = lambdaA/lambdaB
r_original = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([14,12,7,10,10,12,8,10,8,12,14,7,13,9,8,8,10,9,9,11] +                              # r = 0.0001
                                  [33,28,26,30,25,31,33,28,32,29,28,29,25,27,30,31,32,27,27,27] +                     # r = 0.001
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # r = 0.01
                                  [230,238,226,233,225,219,216,219,225,221,217,224,223,219,222,219,213,225,225,229] + # r = 0.1
                                  [331,326,336,340,348,333,345,326,336,328,319,336,326,327,330,332,335,331,320,329]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage
r_inferred = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([300,308,315,304,323,307,319,312,329,312,306,316,300,321,310,308,314,309,304,311] + # r = 0.0001
                                  [261,263,271,257,262,278,270,269,268,256,278,280,270,249,266,274,252,280,273,274] + # r = 0.001
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # r = 0.01
                                  [243,262,246,252,258,241,242,237,247,251,251,240,250,244,240,250,242,243,250,255] + # r = 0.1
                                  [326,325,328,338,348,327,343,325,341,329,320,334,327,327,330,324,333,332,314,329]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying lambda = lambdaA + lambdaB
l_original = {'lambda':np.array([33.86550309051126]*20+[84.66375772627816]*20+[169.32751545255631]*20+[338.65503090511262]*20+[846.63757726278155]*20),
              'cherries':np.array([88,88,91,98,86,90,98,106,96,83,96,83,87,98,98,95,85,96,101,92] +                   # lambda = 33.86550309051126
                                  [97,85,92,87,84,94,96,97,88,93,80,98,95,91,100,91,87,87,90,98] +                    # lambda = 84.66375772627816
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # lambda = 169.32751545255631
                                  [91,89,90,82,94,79,81,89,92,91,90,93,95,92,96,94,91,90,86,94] +                     # lambda = 338.65503090511262
                                  [88,89,89,87,89,87,89,86,85,87,94,84,83,85,84,87,86,84,83,89]                       # lambda = 846.63757726278155
             ).astype(float)/1000} # divide by number of leaves to get percentage
l_inferred = {'lambda':np.array([33.86550309051126]*20+[84.66375772627816]*20+[169.32751545255631]*20+[338.65503090511262]*20+[846.63757726278155]*20),
              'cherries':np.array([215,190,198,191,196,190,204,211,189,184,181,202,189,190,183,199,170,182,189,182] + # lambda = 33.86550309051126
                                  [195,211,200,203,204,205,184,189,182,197,194,198,191,200,190,192,193,200,187,195] + # lambda = 84.66375772627816
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # lambda = 169.32751545255631
                                  [234,223,227,222,232,231,218,225,227,229,223,209,226,237,240,237,227,220,227,221] + # lambda = 338.65503090511262
                                  [233,229,217,222,225,219,217,227,222,219,246,213,233,246,209,210,232,240,218,231]   # lambda = 846.63757726278155
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying sequence length
k_original = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20), # values of length
              'cherries':np.array([89,94,93,93,96,90,99,96,89,88,87,79,96,96,95,88,81,93,85,91] +                     # length = 50
                                  [93,91,92,91,90,88,100,87,89,89,85,98,87,86,86,88,88,94,91,88] +                    # length = 100
                                  [86,87,84,91,92,87,95,93,82,90,95,91,91,89,84,82,96,85,93,95] +                     # length = 200
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # length = 300
                                  [88,86,88,80,94,91,96,95,91,92,80,91,90,102,84,88,97,90,89,86]                      # length = 600
             ).astype(float)/1000} # divide by number of leaves to get percentage
k_inferred = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20), # values of length
              'cherries':np.array([229,240,216,231,204,229,212,212,217,223,219,213,211,207,227,209,222,214,236,238] + # length = 50
                                  [225,238,240,243,233,225,232,244,249,229,252,239,241,222,262,233,227,236,234,248] + # length = 100
                                  [209,221,226,221,221,243,236,238,222,230,228,215,221,233,221,235,242,229,238,223] + # length = 200
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # length = 300
                                  [173,176,178,179,191,182,176,169,185,178,190,182,182,182,175,176,176,175,185,181]   # length = 600
             ).astype(float)/1000} # divide by number of leaves to get percentage

# plot cherries fraction vs. r
handles = [Patch(color='blue',label='Original'),Patch(color='green',label='Inferred'),Patch(color='red',label='Theoretical')]
fig = plt.figure()
ax = sns.boxplot(x='r',y='cherries',data=pd.DataFrame(r_original),order=np.array([-4,-3,-2,-1,0]),color='blue')
sns.boxplot(x='r',y='cherries',data=pd.DataFrame(r_inferred),order=np.array([-4,-3,-2,-1,0]),color='green')
x = np.linspace(-4,0,100)
plt.plot(x+4,cherries_vs_r(10**x),label='Theoretical',linestyle='--',color='red')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}$',fontsize=14)
sns.plt.ylabel('Cherries Fraction',fontsize=14)
sns.plt.title(r'Cherries Fraction vs. $\log_{10}{r}$',fontsize=18)
sns.plt.show()
fig.savefig('cherries-fraction_vs_r.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot cherries fraction vs. lambda
handles = [Patch(color='blue',label='Original'),Patch(color='green',label='Inferred')]
fig = plt.figure()
ax = sns.boxplot(x='lambda',y='cherries',data=pd.DataFrame(l_original),order=np.array([33.86550309051126,84.66375772627816,169.32751545255631,338.65503090511262,846.63757726278155]),color='blue')
sns.boxplot(x='lambda',y='cherries',data=pd.DataFrame(l_inferred),order=np.array([33.86550309051126,84.66375772627816,169.32751545255631,338.65503090511262,846.63757726278155]),color='green')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\lambda = \lambda_A + \lambda_B$',fontsize=14)
sns.plt.ylabel('Cherries Fraction',fontsize=14)
sns.plt.title(r'Cherries Fraction vs. $\lambda$',fontsize=18)
sns.plt.show()
fig.savefig('cherries-fraction_vs_lambda.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot cherries fraction vs. length
handles = [Patch(color='blue',label='Original'),Patch(color='green',label='Inferred')]
fig = plt.figure()
ax = sns.boxplot(x='length',y='cherries',data=pd.DataFrame(k_original),order=np.array([50,100,200,300,600]),color='blue')
sns.boxplot(x='length',y='cherries',data=pd.DataFrame(k_inferred),order=np.array([50,100,200,300,600]),color='green')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel('Sequence Length',fontsize=14)
sns.plt.ylabel('Cherries Fraction',fontsize=14)
sns.plt.title('Cherries Fraction vs. Sequence Length',fontsize=18)
sns.plt.show()
fig.savefig('cherries-fraction_vs_length.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()