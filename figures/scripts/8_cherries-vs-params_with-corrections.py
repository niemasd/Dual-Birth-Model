#! /usr/bin/env python3
'''
Niema Moshiri 2016

Generate plots of fraction of cherries vs. various parameters
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
sns.set_style("ticks")
rcParams['font.family'] = 'serif'
pal = {'theoretical':'#000000', 'simulated':'#0000FF', 'fasttree':'#FF0000', 'raxml':'#00FF00'}
handles = [Patch(color=pal['theoretical'],label='Theoretical'),Patch(color=pal['simulated'],label='Simulated'),Patch(color=pal['fasttree'],label='FastTree'),Patch(color=pal['raxml'],label='RAxML')]
axisY = np.asarray([i/10.0 for i in range(0,5)])

# Expected Number of Cherries as a Function of r
def cherries_vs_r(r):
    return (r**0.5)/(1+r+r**0.5)

# set alpha transparency for axes
def setAlpha(ax,a):
    for art in ax.get_children():
        if isinstance(art, PolyCollection):
            art.set_alpha(a)

# DATASETS
# modifying r = lambdaA/lambdaB (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
r_simulated = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
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
              'cherries':np.array([328,339,333,322,330,325,326,329,339,324,339,342,327,325,337,344,329,343,332,334] + # r = 0.0001
                                  [275,273,274,281,283,282,284,285,290,270,289,290,281,277,264,287,259,286,287,278] + # r = 0.001
                                  [199,215,210,215,211,228,215,192,209,208,219,225,197,206,211,212,209,209,217,200] + # r = 0.01
                                  [243,264,248,253,258,242,241,243,247,251,252,242,255,242,248,248,240,243,256,263] + # r = 0.1
                                  [331,322,330,336,346,326,343,327,338,328,320,332,326,327,332,324,335,330,317,331]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying r = lambdaA/lambdaB (with constant lambda = lambdaA + lambdaB)
r2_simulated = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
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
              'cherries':np.array([288,278,262,280,286,269,288,278,276,280,289,275,276,271,285,275,289,269,265,269] + # r = 0.0001
                                  [234,244,233,244,242,235,238,237,236,244,233,217,251,236,239,243,230,236,224,220] + # r = 0.001
                                  [199,215,210,215,211,228,215,192,209,208,219,225,197,206,211,212,209,209,217,200] + # r = 0.01
                                  [258,266,273,274,259,258,254,260,256,272,259,258,273,260,262,264,263,271,265,264] + # r = 0.1
                                  [331,321,323,327,323,319,324,316,319,335,320,324,322,325,327,331,316,331,338,326]   # r = 1
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying lambda = lambdaA + lambdaB
l_simulated = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
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
              'cherries':np.array([202,187,195,191,182,183,194,205,183,184,183,196,182,182,178,197,164,178,186,178] + # lambda = 33.86550309051126
                                  [193,206,193,189,197,192,182,193,175,194,193,197,195,199,184,193,189,190,185,187] + # lambda = 84.66375772627816
                                  [199,215,210,215,211,228,215,192,209,208,219,225,197,206,211,212,209,209,217,200] + # lambda = 169.32751545255631
                                  [250,247,263,229,248,258,226,237,236,239,233,238,243,252,246,246,241,227,242,240] + # lambda = 338.65503090511262
                                  [274,274,279,273,289,267,272,267,273,271,279,259,263,280,275,265,273,285,279,295]   # lambda = 846.63757726278155
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying sequence length
k_simulated = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
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
              'cherries':np.array([285,293,273,278,267,270,262,280,277,286,275,276,270,277,278,279,276,272,268,277] + # length = 50
                                  [257,250,262,256,252,260,264,255,264,257,265,263,254,250,273,251,252,257,263,256] + # length = 100
                                  [223,225,230,231,229,239,239,238,219,229,240,219,234,242,224,233,240,238,245,229] + # length = 200
                                  [199,215,210,215,211,228,215,192,209,208,219,225,197,206,211,212,209,209,217,200] + # length = 300
                                  [176,175,173,175,189,187,170,170,184,181,178,184,170,182,176,175,174,179,181,177] + # length = 600
                                  [128,140,147,159,146,158,165,146,152,156,138,149,155,146,152,151,140,156,138,145] + # length = 1200
                                  [129,130,130,135,126,121,135,127,129,122,128,130,116,120,127,131,124,118,130,118] + # length = 2400
                                  [104,117,109,109,112,110,119,114,113,122,113,101,122,104,126,115,103,103,121,109]   # length = 4800
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying deviation from ultrametricity
g_simulated = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
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
              'cherries':np.array([225,215,219,208,219,214,209,212,210,215,215,226,210,218,223,226,221,214,203,207] + # gamma = 2.95181735298926
                                  [213,210,203,213,220,228,217,215,205,221,209,218,212,203,226,221,225,225,215,213] + # gamma = 5.90363470597852
                                  [199,215,210,215,211,228,215,192,209,208,219,225,197,206,211,212,209,209,217,200] + # gamma = 29.518173529892621
                                  [213,209,218,214,198,198,223,213,212,215,218,224,219,208,203,199,219,211,202,200] + # gamma = 147.590867649463
                                  [204,210,227,210,204,207,192,213,198,213,223,220,217,212,220,214,215,209,201,215] + # gamma = 295.181735298926
                                  [218,209,210,216,202,220,210,211,219,203,220,211,211,225,229,213,218,214,200,194]   # gamma = infinity
             ).astype(float)/1000} # divide by number of leaves to get percentage

# modifying n
n_simulated = {'n':np.array([25]*20+[50]*20+[250]*20+[500]*20+[1000]*20+[2000]*20+[4000]*20),
              'cherries':np.array([0.12,0.08,0.08,0.16,0.08,0.12,0.08,0.12,0.12,0.08,0.08,0.08,0.12,0.12,0.12,0.08,0.08,0.08,0.08,0.12] +                    # n = 25
                                  [0.08,0.12,0.16,0.14,0.08,0.08,0.1,0.1,0.1,0.1,0.12,0.16,0.12,0.1,0.08,0.12,0.08,0.1,0.12,0.06] +                     # n = 50
                                  [0.1,0.092,0.1,0.092,0.08,0.084,0.084,0.08,0.088,0.096,0.092,0.084,0.112,0.104,0.088,0.092,0.088,0.096,0.108,0.096] +                    # n = 250
                                  [0.098,0.102,0.09,0.098,0.086,0.096,0.096,0.1,0.098,0.092,0.09,0.088,0.096,0.1,0.1,0.092,0.094,0.086,0.09,0.078] +                     # n = 500
                                  [0.088,0.091,0.09,0.088,0.086,0.09,0.09,0.091,0.092,0.094,0.085,0.087,0.088,0.086,0.1,0.088,0.091,0.091,0.098,0.09] +                     # n = 1000
                                  [0.088,0.0895,0.0895,0.0905,0.088,0.086,0.094,0.0905,0.102,0.091,0.087,0.0815,0.093,0.089,0.095,0.089,0.0875,0.0905,0.0955,0.0945] +                     # n = 2000
                                  [0.09175,0.0895,0.09275,0.09425,0.09225,0.09125,0.089,0.0875,0.09225,0.08725,0.089,0.09225,0.09175,0.09125,0.08925,0.09,0.0885,0.09025,0.0915,0.09075]                      # n = 4000
             ).astype(float)} # divide by number of leaves to get percentage
n_fasttree = {'n':np.array([25]*20+[50]*20+[250]*20+[500]*20+[1000]*20+[2000]*20+[4000]*20),
              'cherries':np.array([0.16,0.24,0.16,0.16,0.24,0.2,0.12,0.2,0.2,0.24,0.2,0.12,0.2,0.2,0.24,0.2,0.16,0.2,0.12,0.24] +                    # n = 25
                                  [0.2,0.2,0.2,0.22,0.22,0.14,0.16,0.26,0.22,0.18,0.24,0.2,0.2,0.22,0.2,0.16,0.18,0.18,0.24,0.22] +                     # n = 50
                                  [0.208,0.184,0.212,0.224,0.224,0.224,0.22,0.196,0.228,0.216,0.204,0.208,0.216,0.196,0.192,0.216,0.228,0.188,0.208,0.172] +                    # n = 250
                                  [0.204,0.198,0.218,0.208,0.208,0.19,0.204,0.204,0.192,0.226,0.202,0.226,0.226,0.208,0.22,0.202,0.2,0.2,0.206,0.206] +                     # n = 500
                                  [0.208,0.204,0.216,0.214,0.213,0.216,0.216,0.196,0.207,0.197,0.221,0.219,0.176,0.206,0.205,0.217,0.219,0.21,0.214,0.197] +                     # n = 1000
                                  [0.2215,0.214,0.214,0.2095,0.209,0.2055,0.2055,0.205,0.208,0.206,0.2075,0.219,0.217,0.2105,0.2175,0.199,0.215,0.216,0.211,0.202] +                     # n = 2000
                                  [0.208,0.212,0.21,0.21225,0.21275,0.20925,0.2075,0.213,0.20325,0.2085,0.195,0.2125,0.218,0.207,0.21225,0.212,0.205,0.2075,0.204,0.2105]                      # n = 4000
             ).astype(float)} # divide by number of leaves to get percentage
n_raxml    = {'n':np.array([25]*20+[50]*20+[250]*20+[500]*20+[1000]*20+[2000]*20+[4000]*20),
              'cherries':np.array([0.24,0.16,0.12,0.16,0.24,0.2,0.16,0.2,0.16,0.24,0.2,0.12,0.24,0.16,0.2,0.2,0.12,0.2,0.12,0.2] +                    # n = 25
                                  [0.18,0.2,0.2,0.2,0.22,0.16,0.16,0.3,0.18,0.16,0.24,0.22,0.2,0.18,0.18,0.14,0.2,0.22,0.16,0.22] +                     # n = 50
                                  [0.204,0.184,0.188,0.212,0.188,0.212,0.196,0.184,0.2,0.216,0.192,0.188,0.212,0.18,0.188,0.208,0.18,0.188,0.212,0.192] +                    # n = 250
                                  [0.19,0.21,0.194,0.202,0.198,0.19,0.2,0.208,0.182,0.224,0.188,0.216,0.204,0.218,0.212,0.186,0.192,0.194,0.198,0.192] +                     # n = 500
                                  [0.193,0.19,0.199,0.193,0.197,0.196,0.209,0.19,0.19,0.199,0.205,0.218,0.192,0.199,0.185,0.197,0.203,0.203,0.198,0.189] +                     # n = 1000
                                  [0.199,0.2075,0.1935,0.199,0.19,0.188,0.194,0.2,0.2,0.196,0.197,0.204,0.1955,0.196,0.2075,0.1985,0.192,0.2035,0.201,0.1955] +                     # n = 2000
                                  [0.199,0.20525,0.2005,0.20475,0.19325,0.1915,0.201,0.2,0.19425,0.195,0.1865,0.1965,0.20375,0.19575,0.2,0.20025,0.19,0.199,0.1895,0.19925]                      # n = 4000
             ).astype(float)} # divide by number of leaves to get percentage

# plot Cherry Fraction vs. r (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
ax = sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r_fasttree),order=x,color=pal['fasttree'],width=0.3)
plt.plot(np.asarray([sum(r_fasttree['r'][i:i+20])/20.0 for i in range(0,len(r_fasttree['cherries']),20)])+4,[sum(r_fasttree['cherries'][i:i+20])/20.0 for i in range(0,len(r_fasttree['cherries']),20)],color=pal['fasttree'],linestyle='--',linewidth=3)
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r_raxml),order=x,color=pal['raxml'],width=0.3)
plt.plot(np.asarray([sum(r_raxml['r'][i:i+20])/20.0 for i in range(0,len(r_raxml['cherries']),20)])+4,[sum(r_raxml['cherries'][i:i+20])/20.0 for i in range(0,len(r_raxml['cherries']),20)],color=pal['raxml'],linestyle='--',linewidth=3)
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r_simulated),order=x,color=pal['simulated'],width=0.3)
plt.plot(np.asarray([sum(r_simulated['r'][i:i+20])/20.0 for i in range(0,len(r_simulated['cherries']),20)])+4,[sum(r_simulated['cherries'][i:i+20])/20.0 for i in range(0,len(r_simulated['cherries']),20)],color=pal['simulated'],linestyle='--',linewidth=3)
setAlpha(ax,0.5)
x = np.linspace(-4,0,100)
plt.plot(x+4,cherries_vs_r(10**x),label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}$',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title(r'Cherry Fraction vs. $\log_{10}{r}$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_r_const-exp-branch-length_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Cherry Fraction vs. r (with constant lambda = lambdaA + lambdaB)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
ax = sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r2_fasttree),order=x,color=pal['fasttree'],width=0.3)
plt.plot(np.asarray([sum(r2_fasttree['r'][i:i+20])/20.0 for i in range(0,len(r2_fasttree['cherries']),20)])+4,[sum(r2_fasttree['cherries'][i:i+20])/20.0 for i in range(0,len(r2_fasttree['cherries']),20)],color=pal['fasttree'],linestyle='--',linewidth=3)
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r2_raxml),order=x,color=pal['raxml'],width=0.3)
plt.plot(np.asarray([sum(r2_raxml['r'][i:i+20])/20.0 for i in range(0,len(r2_raxml['cherries']),20)])+4,[sum(r2_raxml['cherries'][i:i+20])/20.0 for i in range(0,len(r2_raxml['cherries']),20)],color=pal['raxml'],linestyle='--',linewidth=3)
sns.violinplot(x='r',y='cherries',data=pd.DataFrame(r2_simulated),order=x,color=pal['simulated'],width=0.3)
plt.plot(np.asarray([sum(r2_simulated['r'][i:i+20])/20.0 for i in range(0,len(r2_simulated['cherries']),20)])+4,[sum(r2_simulated['cherries'][i:i+20])/20.0 for i in range(0,len(r2_simulated['cherries']),20)],color=pal['simulated'],linestyle='--',linewidth=3)
setAlpha(ax,0.5)
x = np.linspace(-4,0,100)
plt.plot(x+4,cherries_vs_r(10**x),label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(\lambda = \lambda_A + \lambda_B = 169\right)$',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title(r'Cherry Fraction vs. $\log_{10}{r}\ \left(\lambda=\lambda_A+\lambda_B=169\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_r_const-lambda_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Cherry Fraction vs. lambda
fig = plt.figure()
x = np.array([33.866,84.664,169.328,338.655,846.638])
ax = sns.violinplot(x='lambda',y='cherries',data=pd.DataFrame(l_fasttree),order=x,color=pal['fasttree'],width=0.3)
sns.pointplot(np.asarray([sum(l_fasttree['lambda'][i:i+20])/20.0 for i in range(0,len(l_fasttree['cherries']),20)]),[sum(l_fasttree['cherries'][i:i+20])/20.0 for i in range(0,len(l_fasttree['cherries']),20)],color=pal['fasttree'],linestyles=['--'],linewidth=3)
sns.violinplot(x='lambda',y='cherries',data=pd.DataFrame(l_raxml),order=x,color=pal['raxml'],width=0.3)
sns.pointplot(np.asarray([sum(l_raxml['lambda'][i:i+20])/20.0 for i in range(0,len(l_raxml['cherries']),20)]),[sum(l_raxml['cherries'][i:i+20])/20.0 for i in range(0,len(l_raxml['cherries']),20)],color=pal['raxml'],linestyles=['--'],linewidth=3)
sns.violinplot(x='lambda',y='cherries',data=pd.DataFrame(l_simulated),order=x,color=pal['simulated'],width=0.3)
sns.pointplot(np.asarray([sum(l_simulated['lambda'][i:i+20])/20.0 for i in range(0,len(l_simulated['cherries']),20)]),[sum(l_simulated['cherries'][i:i+20])/20.0 for i in range(0,len(l_simulated['cherries']),20)],color=pal['simulated'],linestyles=['--'],linewidth=3)
setAlpha(ax,0.5)
x = np.linspace(-100,1000,1100)
plt.plot(x,np.array([cherries_vs_r(0.01)]*len(x)),label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\lambda = \lambda_A + \lambda_B$',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title(r'Cherry Fraction vs. $\lambda$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_lambda_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Cherry Fraction vs. length
fig = plt.figure()
x = np.array([50,100,200,300,600,1200,2400,4800])
ax = sns.violinplot(x='length',y='cherries',data=pd.DataFrame(k_fasttree),order=x,color=pal['fasttree'],width=0.3)
sns.pointplot(np.asarray([sum(k_fasttree['length'][i:i+20])/20 for i in range(0,len(k_fasttree['cherries']),20)]),[sum(k_fasttree['cherries'][i:i+20])/20.0 for i in range(0,len(k_fasttree['cherries']),20)],color=pal['fasttree'],linestyles=['--'],linewidth=3)
sns.violinplot(x='length',y='cherries',data=pd.DataFrame(k_raxml),order=x,color=pal['raxml'],width=0.3)
sns.pointplot(np.asarray([sum(k_raxml['length'][i:i+20])/20 for i in range(0,len(k_raxml['cherries']),20)]),[sum(k_raxml['cherries'][i:i+20])/20.0 for i in range(0,len(k_raxml['cherries']),20)],color=pal['raxml'],linestyles=['--'],linewidth=3)
sns.violinplot(x='length',y='cherries',data=pd.DataFrame(k_simulated),order=x,color=pal['simulated'],width=0.3)
sns.pointplot(np.asarray([sum(k_simulated['length'][i:i+20])/20 for i in range(0,len(k_simulated['cherries']),20)]),[sum(k_simulated['cherries'][i:i+20])/20.0 for i in range(0,len(k_simulated['cherries']),20)],color=pal['simulated'],linestyles=['--'],linewidth=3)
setAlpha(ax,0.5)
x = np.linspace(-100,5000,5100)
plt.plot(x,np.array([cherries_vs_r(0.01)]*len(x)),label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel('Sequence Length',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title('Cherry Fraction vs. Sequence Length',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_length_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Cherry Fraction vs. gamma rate
fig = plt.figure()
x = np.array([2.952,5.904,29.518,147.591,295.182,float('inf')])
ax = sns.violinplot(x='gammarate',y='cherries',data=pd.DataFrame(g_fasttree),order=x,color=pal['fasttree'],width=0.3)
sns.pointplot(np.asarray([sum(g_fasttree['gammarate'][i:i+20])/20.0 for i in range(0,len(g_fasttree['cherries']),20)]),[sum(g_fasttree['cherries'][i:i+20])/20.0 for i in range(0,len(g_fasttree['cherries']),20)],color=pal['fasttree'],linestyles=['--'],linewidth=3)
sns.violinplot(x='gammarate',y='cherries',data=pd.DataFrame(g_raxml),order=x,color=pal['raxml'],width=0.3)
sns.pointplot(np.asarray([sum(g_raxml['gammarate'][i:i+20])/20.0 for i in range(0,len(g_raxml['cherries']),20)]),[sum(g_raxml['cherries'][i:i+20])/20.0 for i in range(0,len(g_raxml['cherries']),20)],color=pal['raxml'],linestyles=['--'],linewidth=3)
sns.violinplot(x='gammarate',y='cherries',data=pd.DataFrame(g_simulated),order=x,color=pal['simulated'],width=0.3)
sns.pointplot(np.asarray([sum(g_simulated['gammarate'][i:i+20])/20.0 for i in range(0,len(g_simulated['cherries']),20)]),[sum(g_simulated['cherries'][i:i+20])/20.0 for i in range(0,len(g_simulated['cherries']),20)],color=pal['simulated'],linestyles=['--'],linewidth=3)
setAlpha(ax,0.5)
x = np.linspace(-100,1000,5000)
plt.plot(x,np.array([cherries_vs_r(0.01)]*len(x)),label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'Gamma Distribution Rate $\left(\alpha\right)$',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title('Cherry Fraction vs. Ultrametricity',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_gammarate_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Cherry Fraction vs. n
fig = plt.figure()
x = np.array([25,50,250,500,1000,2000,4000])
ax = sns.violinplot(x='n',y='cherries',data=pd.DataFrame(n_fasttree),order=x,color=pal['fasttree'],width=0.3)
sns.pointplot(np.asarray([sum(n_fasttree['n'][i:i+20])/20.0 for i in range(0,len(n_fasttree['cherries']),20)]),[sum(n_fasttree['cherries'][i:i+20])/20.0 for i in range(0,len(n_fasttree['cherries']),20)],color=pal['fasttree'],linestyles=['--'],linewidth=3)
sns.violinplot(x='n',y='cherries',data=pd.DataFrame(n_raxml),order=x,color=pal['raxml'],width=0.3)
sns.pointplot(np.asarray([sum(n_raxml['n'][i:i+20])/20.0 for i in range(0,len(n_raxml['cherries']),20)]),[sum(n_raxml['cherries'][i:i+20])/20.0 for i in range(0,len(n_raxml['cherries']),20)],color=pal['raxml'],linestyles=['--'],linewidth=3)
sns.violinplot(x='n',y='cherries',data=pd.DataFrame(n_simulated),order=x,color=pal['simulated'],width=0.3)
sns.pointplot(np.asarray([sum(n_simulated['n'][i:i+20])/20.0 for i in range(0,len(n_simulated['cherries']),20)]),[sum(n_simulated['cherries'][i:i+20])/20.0 for i in range(0,len(n_simulated['cherries']),20)],color=pal['simulated'],linestyles=['--'],linewidth=3)
setAlpha(ax,0.5)
x = np.linspace(-100,1000,5000)
plt.plot(x,np.array([cherries_vs_r(0.01)]*len(x)),label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$n$',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title(r'Cherry Fraction vs. $n$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherries-fraction_vs_n_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()