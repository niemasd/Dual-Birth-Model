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
r_inferred = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([300,308,315,304,323,307,319,312,329,312,306,316,300,321,310,308,314,309,304,311] + # r = 0.0001
                                  [261,263,271,257,262,278,270,269,268,256,278,280,270,249,266,274,252,280,273,274] + # r = 0.001
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # r = 0.01
                                  [243,262,246,252,258,241,242,237,247,251,251,240,250,244,240,250,242,243,250,255] + # r = 0.1
                                  [326,325,328,338,348,327,343,325,341,329,320,334,327,327,330,324,333,332,314,329]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying r = lambdaA/lambdaB (with constant lambda = lambdaA + lambdaB)
r2_original = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([12,8,9,9,10,11,11,11,10,10,9,11,11,11,9,9,7,14,11,9] +                             # r = 0.0001
                                  [36,36,36,30,26,25,34,32,31,30,26,30,32,33,33,25,35,29,36,32] +                     # r = 0.001
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # r = 0.01
                                  [220,232,233,225,232,221,221,223,224,230,234,218,230,218,227,227,227,231,223,219] + # r = 0.1
                                  [336,319,341,338,325,323,328,324,327,338,336,330,319,336,333,338,332,334,347,331]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage
r2_inferred = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([292,295,285,275,309,289,306,297,298,285,296,298,290,286,291,296,296,282,277,278] + # r = 0.0001
                                  [238,248,238,257,245,232,264,239,252,252,243,223,241,232,225,243,235,244,231,228] + # r = 0.001
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # r = 0.01
                                  [253,261,268,268,242,247,230,249,243,256,251,245,260,256,265,254,252,257,261,244] + # r = 0.1
                                  [313,303,308,314,303,307,307,290,300,313,295,303,304,306,303,310,288,300,324,310]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying lambda = lambdaA + lambdaB
l_original = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'cherries':np.array([88,88,91,98,86,90,98,106,96,83,96,83,87,98,98,95,85,96,101,92] +                   # lambda = 33.86550309051126
                                  [97,85,92,87,84,94,96,97,88,93,80,98,95,91,100,91,87,87,90,98] +                    # lambda = 84.66375772627816
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # lambda = 169.32751545255631
                                  [91,89,90,82,94,79,81,89,92,91,90,93,95,92,96,94,91,90,86,94] +                     # lambda = 338.65503090511262
                                  [88,89,89,87,89,87,89,86,85,87,94,84,83,85,84,87,86,84,83,89]                       # lambda = 846.63757726278155
             ).astype(float)/1000} # divide by number of leaves to get percentage
l_inferred = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'cherries':np.array([215,190,198,191,196,190,204,211,189,184,181,202,189,190,183,199,170,182,189,182] + # lambda = 33.86550309051126
                                  [195,211,200,203,204,205,184,189,182,197,194,198,191,200,190,192,193,200,187,195] + # lambda = 84.66375772627816
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # lambda = 169.32751545255631
                                  [234,223,227,222,232,231,218,225,227,229,223,209,226,237,240,237,227,220,227,221] + # lambda = 338.65503090511262
                                  [233,229,217,222,225,219,217,227,222,219,246,213,233,246,209,210,232,240,218,231]   # lambda = 846.63757726278155
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
k_inferred = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'cherries':np.array([229,240,216,231,204,229,212,212,217,223,219,213,211,207,227,209,222,214,236,238] + # length = 50
                                  [225,238,240,243,233,225,232,244,249,229,252,239,241,222,262,233,227,236,234,248] + # length = 100
                                  [209,221,226,221,221,243,236,238,222,230,228,215,221,233,221,235,242,229,238,223] + # length = 200
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # length = 300
                                  [173,176,178,179,191,182,176,169,185,178,190,182,182,182,175,176,176,175,185,181] + # length = 600
                                  [130,141,154,163,145,159,164,150,159,156,144,152,161,148,153,149,143,161,141,144] + # length = 1200
                                  [131,134,133,137,125,123,134,125,131,123,128,133,113,121,128,134,128,122,131,118] + # length = 2400
                                  [106,121,113,109,111,113,120,116,115,121,116,104,124,103,131,115,105,104,119,111]   # length = 4800
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
g_inferred = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'cherries':np.array([214,210,207,208,203,204,202,214,200,206,210,229,219,220,223,229,214,216,197,220] + # gamma = 2.95181735298926
                                  [210,208,204,201,206,213,219,211,209,218,192,210,192,205,213,214,212,225,212,215] + # gamma = 5.90363470597852
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # gamma = 29.518173529892621
                                  [211,200,220,196,195,196,228,212,210,211,217,215,214,202,207,204,216,220,206,201] + # gamma = 147.590867649463
                                  [209,204,220,205,197,211,184,209,197,205,223,217,214,214,215,208,205,202,211,205] + # gamma = 295.181735298926
                                  [207,210,207,210,201,203,204,210,224,204,220,206,209,217,227,214,217,204,203,196]   # gamma = infinity
             ).astype(float)/1000} # divide by number of leaves to get percentage

# plot cherries fraction vs. r (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred'),Patch(color='#D65F5F',label='Theoretical')]
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
#ax = sns.boxplot(x='r',y='cherries',data=pd.DataFrame(r_original),order=x,color='#597DBE')
ax = sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r_original),order=x,color='#597DBE')
#sns.boxplot(x='r',y='cherries',data=pd.DataFrame(r_inferred),order=x,color='#76BF72')
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r_inferred),order=x,color='#76BF72')
x = np.linspace(-4,0,100)
plt.plot(x+4,cherries_vs_r(10**x),label='Theoretical',linestyle='--',color='#D65F5F')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(E(l_b)=0.298\right)$',fontsize=14)
sns.plt.ylabel('Cherries Fraction',fontsize=14)
sns.plt.title(r'Cherries Fraction vs. $\log_{10}{r}\ \left(E(l_b)=0.298\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_r_const-exp-branch-length.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot cherries fraction vs. r (with constant lambda = lambdaA + lambdaB)
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred'),Patch(color='#D65F5F',label='Theoretical')]
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
#ax = sns.boxplot(x='r',y='cherries',data=pd.DataFrame(r_original),order=x,color='#597DBE')
ax = sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r2_original),order=x,color='#597DBE')
#sns.boxplot(x='r',y='cherries',data=pd.DataFrame(r_inferred),order=x,color='#76BF72')
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r2_inferred),order=x,color='#76BF72')
x = np.linspace(-4,0,100)
plt.plot(x+4,cherries_vs_r(10**x),label='Theoretical',linestyle='--',color='#D65F5F')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(\lambda = \lambda_A + \lambda_B = 169\right)$',fontsize=14)
sns.plt.ylabel('Cherries Fraction',fontsize=14)
sns.plt.title(r'Cherries Fraction vs. $\log_{10}{r}\ \left(\lambda=\lambda_A+\lambda_B=169\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_r_const-lambda.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot cherries fraction vs. lambda
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred'),Patch(color='#D65F5F',label='Theoretical')]
fig = plt.figure()
x = np.array([33.866,84.664,169.328,338.655,846.638])
#ax = sns.boxplot(x='lambda',y='cherries',data=pd.DataFrame(l_original),order=x,color='#597DBE')
ax = sns.violinplot(x='lambda',y='cherries',data=pd.DataFrame(l_original),order=x,color='#597DBE')
#sns.boxplot(x='lambda',y='cherries',data=pd.DataFrame(l_inferred),order=x,color='#76BF72')
sns.violinplot(x='lambda',y='cherries',data=pd.DataFrame(l_inferred),order=x,color='#76BF72')
x = np.linspace(-100,1000,1100)
plt.plot(x,np.array([cherries_vs_r(0.01)]*len(x)),label='Theoretical',linestyle='--',color='#D65F5F')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\lambda = \lambda_A + \lambda_B$',fontsize=14)
sns.plt.ylabel('Cherries Fraction',fontsize=14)
sns.plt.title(r'Cherries Fraction vs. $\lambda$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_lambda.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot cherries fraction vs. length
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred'),Patch(color='#D65F5F',label='Theoretical')]
fig = plt.figure()
x = np.array([50,100,200,300,600,1200,2400,4800])
#ax = sns.boxplot(x='length',y='cherries',data=pd.DataFrame(k_original),order=x,color='#597DBE')
ax = sns.violinplot(x='length',y='cherries',data=pd.DataFrame(k_original),order=x,color='#597DBE')
#sns.boxplot(x='length',y='cherries',data=pd.DataFrame(k_inferred),order=x,color='#76BF72')
sns.violinplot(x='length',y='cherries',data=pd.DataFrame(k_inferred),order=x,color='#76BF72')
x = np.linspace(-100,5000,5100)
plt.plot(x,np.array([cherries_vs_r(0.01)]*len(x)),label='Theoretical',linestyle='--',color='#D65F5F')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel('Sequence Length',fontsize=14)
sns.plt.ylabel('Cherries Fraction',fontsize=14)
sns.plt.title('Cherries Fraction vs. Sequence Length',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_length.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot cherries fraction vs. gamma rate
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred'),Patch(color='#D65F5F',label='Theoretical')]
fig = plt.figure()
x = np.array([2.952,5.904,29.518,147.591,295.182,float('inf')])
#ax = sns.boxplot(x='gammarate',y='cherries',data=pd.DataFrame(g_original),order=x,color='#597DBE')
ax = sns.violinplot(x='gammarate',y='cherries',data=pd.DataFrame(g_original),order=x,color='#597DBE')
#sns.boxplot(x='gammarate',y='cherries',data=pd.DataFrame(g_inferred),order=x,color='#76BF72')
sns.violinplot(x='gammarate',y='cherries',data=pd.DataFrame(g_inferred),order=x,color='#76BF72')
x = np.linspace(-100,1000,5000)
plt.plot(x,np.array([cherries_vs_r(0.01)]*len(x)),label='Theoretical',linestyle='--',color='#D65F5F')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'Gamma Distribution Rate $\left(\alpha\right)$',fontsize=14)
sns.plt.ylabel('Cherries Fraction',fontsize=14)
sns.plt.title('Cherries Fraction vs. Deviation from Ultrametricity',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_gammarate.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()