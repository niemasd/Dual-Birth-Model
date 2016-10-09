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
r_fasttree = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([300,308,315,304,323,307,319,312,329,312,306,316,300,321,310,308,314,309,304,311] + # r = 0.0001
                                  [261,263,271,257,262,278,270,269,268,256,278,280,270,249,266,274,252,280,273,274] + # r = 0.001
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # r = 0.01
                                  [243,262,246,252,258,241,242,237,247,251,251,240,250,244,240,250,242,243,250,255] + # r = 0.1
                                  [326,325,328,338,348,327,343,325,341,329,320,334,327,327,330,324,333,332,314,329]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage
r_raxml    = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([323,334,327,320,323,323,325,325,332,314,330,334,317,320,335,334,320,332,316,326] + # r = 0.0001
                                  [261,257,262,261,249,258,265,269,272,241,273,274,264,258,243,274,237,264,271,266] + # r = 0.001
                                  [193,190,199,193,197,196,209,190,190,199,205,218,192,199,185,197,203,203,198,189] + # r = 0.01
                                  [240,256,244,250,253,239,242,238,242,240,241,237,250,236,244,244,235,237,254,256] + # r = 0.1
                                  [329,319,327,332,348,325,343,320,338,322,317,329,323,326,329,322,335,329,312,328]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying r = lambdaA/lambdaB (with constant lambda = lambdaA + lambdaB)
r2_original = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([12,8,9,9,10,11,11,11,10,10,9,11,11,11,9,9,7,14,11,9] +                             # r = 0.0001
                                  [36,36,36,30,26,25,34,32,31,30,26,30,32,33,33,25,35,29,36,32] +                     # r = 0.001
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # r = 0.01
                                  [220,232,233,225,232,221,221,223,224,230,234,218,230,218,227,227,227,231,223,219] + # r = 0.1
                                  [336,319,341,338,325,323,328,324,327,338,336,330,319,336,333,338,332,334,347,331]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage
r2_fasttree = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([292,295,285,275,309,289,306,297,298,285,296,298,290,286,291,296,296,282,277,278] + # r = 0.0001
                                  [238,248,238,257,245,232,264,239,252,252,243,223,241,232,225,243,235,244,231,228] + # r = 0.001
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # r = 0.01
                                  [253,261,268,268,242,247,230,249,243,256,251,245,260,256,265,254,252,257,261,244] + # r = 0.1
                                  [313,303,308,314,303,307,307,290,300,313,295,303,304,306,303,310,288,300,324,310]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage
r2_raxml   = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'cherries':np.array([272,261,246,264,278,248,263,273,250,258,285,259,273,255,267,260,276,243,247,257] + # r = 0.0001
                                  [223,220,224,239,225,226,225,222,219,238,220,214,236,218,221,223,213,218,215,210] + # r = 0.001
                                  [193,190,199,193,197,196,209,190,190,199,205,218,192,199,185,197,203,203,198,189] + # r = 0.01
                                  [243,253,260,262,249,246,253,244,250,265,252,245,255,254,253,254,247,259,252,250] + # r = 0.1
                                  [329,314,322,323,320,314,319,314,312,329,317,317,313,315,318,321,310,326,332,312]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying lambda = lambdaA + lambdaB
l_original = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'cherries':np.array([88,88,91,98,86,90,98,106,96,83,96,83,87,98,98,95,85,96,101,92] +                   # lambda = 33.86550309051126
                                  [97,85,92,87,84,94,96,97,88,93,80,98,95,91,100,91,87,87,90,98] +                    # lambda = 84.66375772627816
                                  [88,91,90,88,86,90,90,91,92,94,85,87,88,86,100,88,91,91,98,90] +                    # lambda = 169.32751545255631
                                  [91,89,90,82,94,79,81,89,92,91,90,93,95,92,96,94,91,90,86,94] +                     # lambda = 338.65503090511262
                                  [88,89,89,87,89,87,89,86,85,87,94,84,83,85,84,87,86,84,83,89]                       # lambda = 846.63757726278155
             ).astype(float)/1000} # divide by number of leaves to get percentage
l_fasttree = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'cherries':np.array([215,190,198,191,196,190,204,211,189,184,181,202,189,190,183,199,170,182,189,182] + # lambda = 33.86550309051126
                                  [195,211,200,203,204,205,184,189,182,197,194,198,191,200,190,192,193,200,187,195] + # lambda = 84.66375772627816
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # lambda = 169.32751545255631
                                  [234,223,227,222,232,231,218,225,227,229,223,209,226,237,240,237,227,220,227,221] + # lambda = 338.65503090511262
                                  [233,229,217,222,225,219,217,227,222,219,246,213,233,246,209,210,232,240,218,231]   # lambda = 846.63757726278155
             ).astype(float)/1000} # divide by number of leaves to get percentage
l_raxml    = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'cherries':np.array([200,186,190,185,183,183,194,208,190,184,180,185,182,184,177,194,170,182,181,180] + # lambda = 33.86550309051126
                                  [195,204,191,184,190,192,184,186,174,185,188,194,195,195,186,189,188,198,172,194] + # lambda = 84.66375772627816
                                  [193,190,199,193,197,196,209,190,190,199,205,218,192,199,185,197,203,203,198,189] + # lambda = 169.32751545255631
                                  [241,235,236,216,223,237,199,226,216,211,208,226,224,236,223,239,225,209,221,221] + # lambda = 338.65503090511262
                                  [270,266,263,262,286,257,267,255,263,264,266,255,256,272,260,259,256,271,263,281]   # lambda = 846.63757726278155
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
k_fasttree = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'cherries':np.array([229,240,216,231,204,229,212,212,217,223,219,213,211,207,227,209,222,214,236,238] + # length = 50
                                  [225,238,240,243,233,225,232,244,249,229,252,239,241,222,262,233,227,236,234,248] + # length = 100
                                  [209,221,226,221,221,243,236,238,222,230,228,215,221,233,221,235,242,229,238,223] + # length = 200
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # length = 300
                                  [173,176,178,179,191,182,176,169,185,178,190,182,182,182,175,176,176,175,185,181] + # length = 600
                                  [130,141,154,163,145,159,164,150,159,156,144,152,161,148,153,149,143,161,141,144] + # length = 1200
                                  [131,134,133,137,125,123,134,125,131,123,128,133,113,121,128,134,128,122,131,118] + # length = 2400
                                  [106,121,113,109,111,113,120,116,115,121,116,104,124,103,131,115,105,104,119,111]   # length = 4800
             ).astype(float)/1000} # divide by number of leaves to get percentage
k_raxml    = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'cherries':np.array([279,286,267,280,260,268,262,269,268,278,269,266,272,274,273,276,265,263,271,279] + # length = 50
                                  [255,245,257,237,240,240,254,240,252,251,259,253,243,250,256,235,250,253,253,255] + # length = 100
                                  [198,215,213,213,214,221,214,221,208,208,222,206,216,225,204,222,224,220,233,219] + # length = 200
                                  [193,190,199,193,197,196,209,190,190,199,205,218,192,199,185,197,203,203,198,189] + # length = 300
                                  [168,154,169,170,181,176,170,170,175,172,170,171,162,182,171,177,165,172,174,170] + # length = 600
                                  [140,136,143,154,147,153,166,162,153,151,141,152,154,153,152,146,150,157,140,142] + # length = 1200
                                  [136,135,129,138,133,128,135,128,131,128,137,137,128,125,128,138,133,118,135,128] + # length = 2400
                                  [112,124,114,117,118,116,126,118,125,128,121,106,130,113,128,119,113,110,129,116]   # length = 4800
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
g_fasttree = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'cherries':np.array([214,210,207,208,203,204,202,214,200,206,210,229,219,220,223,229,214,216,197,220] + # gamma = 2.95181735298926
                                  [210,208,204,201,206,213,219,211,209,218,192,210,192,205,213,214,212,225,212,215] + # gamma = 5.90363470597852
                                  [208,204,216,214,213,216,216,196,207,197,221,219,176,206,205,217,219,210,214,197] + # gamma = 29.518173529892621
                                  [211,200,220,196,195,196,228,212,210,211,217,215,214,202,207,204,216,220,206,201] + # gamma = 147.590867649463
                                  [209,204,220,205,197,211,184,209,197,205,223,217,214,214,215,208,205,202,211,205] + # gamma = 295.181735298926
                                  [207,210,207,210,201,203,204,210,224,204,220,206,209,217,227,214,217,204,203,196]   # gamma = infinity
             ).astype(float)/1000} # divide by number of leaves to get percentage
g_raxml    = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'cherries':np.array([212,196,204,200,202,196,199,205,194,205,202,215,206,203,213,207,218,206,194,193] + # gamma = 2.95181735298926
                                  [199,195,189,202,211,214,202,206,195,212,191,198,188,190,202,205,209,208,198,202] + # gamma = 5.90363470597852
                                  [193,190,199,193,197,196,209,190,190,199,205,218,192,199,185,197,203,203,198,189] + # gamma = 29.518173529892621
                                  [196,188,205,196,187,188,203,198,190,211,217,207,211,189,195,192,203,195,185,189] + # gamma = 147.590867649463
                                  [189,187,210,203,184,188,184,203,179,193,211,196,195,202,203,197,200,191,192,203] + # gamma = 295.181735298926
                                  [208,201,197,209,194,202,194,193,209,193,208,189,191,203,209,192,196,185,194,186]   # gamma = infinity
             ).astype(float)/1000} # divide by number of leaves to get percentage

# plot cherries fraction vs. r (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
handles = [Patch(color='#597DBE',label='Simulated'),Patch(color='#76BF72',label='FastTree'),Patch(color='#B47CC7',label='RAxML'),Patch(color='#D65F5F',label='Theoretical')]
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
ax = sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r_original),order=x,color='#597DBE')
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r_fasttree),order=x,color='#76BF72')
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r_raxml),order=x,color='#B47CC7')
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
handles = [Patch(color='#597DBE',label='Simulated'),Patch(color='#76BF72',label='FastTree'),Patch(color='#B47CC7',label='RAxML'),Patch(color='#D65F5F',label='Theoretical')]
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
ax = sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r2_original),order=x,color='#597DBE')
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r2_fasttree),order=x,color='#76BF72')
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r2_raxml),order=x,color='#B47CC7')
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
handles = [Patch(color='#597DBE',label='Simulated'),Patch(color='#76BF72',label='FastTree'),Patch(color='#B47CC7',label='RAxML'),Patch(color='#D65F5F',label='Theoretical')]
fig = plt.figure()
x = np.array([33.866,84.664,169.328,338.655,846.638])
ax = sns.violinplot(x='lambda',y='cherries',data=pd.DataFrame(l_original),order=x,color='#597DBE')
sns.violinplot(x='lambda',y='cherries',data=pd.DataFrame(l_fasttree),order=x,color='#76BF72')
sns.violinplot(x='lambda',y='cherries',data=pd.DataFrame(l_raxml),order=x,color='#B47CC7')
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
handles = [Patch(color='#597DBE',label='Simulated'),Patch(color='#76BF72',label='FastTree'),Patch(color='#B47CC7',label='RAxML'),Patch(color='#D65F5F',label='Theoretical')]
fig = plt.figure()
x = np.array([50,100,200,300,600,1200,2400,4800])
ax = sns.violinplot(x='length',y='cherries',data=pd.DataFrame(k_original),order=x,color='#597DBE')
sns.violinplot(x='length',y='cherries',data=pd.DataFrame(k_fasttree),order=x,color='#76BF72')
sns.violinplot(x='length',y='cherries',data=pd.DataFrame(k_raxml),order=x,color='#B47CC7')
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
handles = [Patch(color='#597DBE',label='Simulated'),Patch(color='#76BF72',label='FastTree'),Patch(color='#B47CC7',label='RAxML'),Patch(color='#D65F5F',label='Theoretical')]
fig = plt.figure()
x = np.array([2.952,5.904,29.518,147.591,295.182,float('inf')])
ax = sns.violinplot(x='gammarate',y='cherries',data=pd.DataFrame(g_original),order=x,color='#597DBE')
sns.violinplot(x='gammarate',y='cherries',data=pd.DataFrame(g_fasttree),order=x,color='#76BF72')
sns.violinplot(x='gammarate',y='cherries',data=pd.DataFrame(g_raxml),order=x,color='#B47CC7')
x = np.linspace(-100,1000,5000)
plt.plot(x,np.array([cherries_vs_r(0.01)]*len(x)),label='Theoretical',linestyle='--',color='#D65F5F')
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'Gamma Distribution Rate $\left(\alpha\right)$',fontsize=14)
sns.plt.ylabel('Cherries Fraction',fontsize=14)
sns.plt.title('Cherries Fraction vs. Deviation from Ultrametricity',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_gammarate.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()