#! /usr/bin/env python
'''
Niema Moshiri 2016

Generate plots of Tree Error (MS) vs. various parameters
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
pal = {'simulated':'#597DBE', 'fasttree':'#FF9980', 'raxml':'#A2B7C3'}
handles = [Patch(color=pal['fasttree'],label='FastTree'),Patch(color=pal['raxml'],label='RAxML')]

# DATASETS
# modifying r = lambdaA/lambdaB (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
r_fasttree = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'MS':np.array([65055,64640,90159,72707,68420,50961,94463,69734,92656,58516,60214,79300,55340,70843,68160,67268,86080,95909,81511,53340] + # r = 0.0001
                            [22817,25837,23348,31616,25453,24067,33668,44108,22593,24719,28680,25876,29271,23406,18751,23906,23830,38465,29845,26527] + # r = 0.001
                            [6002,5523,6755,7341,8767,5126,9399,5655,6715,7473,6666,9834,6338,5644,6227,6967,5968,8148,5411,8730] +                     # r = 0.01
                            [1715,1642,1788,2068,2235,1863,1845,1418,1737,2383,1969,2257,1744,3219,2751,1905,1892,2379,1591,2465] +                     # r = 0.1
                            [1136,1293,771,1272,1222,1495,1349,918,869,1325,1653,1449,988,1220,941,1349,1509,1277,1707,1430]                            # r = 1
             ).astype(float)}
r_raxml    = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'MS':np.array([64781,63074,91005,70498,68701,48968,93921,69818,97273,59828,61568,83034,56376,70333,68953,69100,88350,92555,81952,54538] + # r = 0.0001
                            [23860,25118,21035,27778,23753,23742,32922,39034,22083,21444,28900,25601,26019,25420,17402,23851,21679,34572,30735,25327] + # r = 0.001
                            [5129,4688,6231,7071,7630,4850,7777,4751,5583,6921,5921,10314,7098,5400,5934,6540,5831,7817,4656,8617] +                    # r = 0.01
                            [2058,1549,1675,1821,1926,1786,1732,1748,1533,2312,2014,2067,1785,2870,2702,1587,1898,3099,1472,2663] +                     # r = 0.1
                            [705,1086,807,1177,766,1407,1339,934,907,1239,1776,1473,659,1258,1010,1239,1440,1273,1697,1263]                             # r = 1
             ).astype(float)}

# modifying r = lambdaA/lambdaB (with constant lambda = lambdaA + lambdaB)
r2_fasttree = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
               'MS':np.array([58523,75820,68606,77836,82539,83870,57514,71509,70890,68886,81589,75796,69577,65998,73474,83591,77028,43364,58471,50778] + # r = 0.0001
                             [25457,30857,28651,30879,31067,19080,25122,26105,27194,20531,30303,18684,24781,25912,23032,28442,19319,27912,33688,17288] + # r = 0.001
                             [6002,5523,6755,7341,8767,5126,9399,5655,6715,7473,6666,9834,6338,5644,6227,6967,5968,8148,5411,8730] +                     # r = 0.01
                             [2206,2444,2107,2815,2436,2789,2936,2466,3103,2510,2445,2843,3123,2907,2860,2888,2373,3265,2296,2827] +                     # r = 0.1
                             [3023,2262,2112,3079,2302,2745,2554,2306,2951,2848,3043,2080,2787,3218,2851,2753,3303,2646,2424,2578]                       # r = 1
              ).astype(float)}
r2_raxml    = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
               'MS':np.array([54365,70472,66901,71249,75505,75171,52406,67956,60520,62645,72208,70638,67691,60504,73715,80131,71177,39152,54748,46638] + # r = 0.0001
                             [22120,25224,28913,25204,27094,16505,23174,21393,24119,18232,29357,18151,22356,24675,22164,26725,17935,22326,28048,15067] + # r = 0.001
                             [5129,4688,6231,7071,7630,4850,7777,4751,5583,6921,5921,10314,7098,5400,5934,6540,5831,7817,4656,8617] +                    # r = 0.01
                             [2318,2413,2006,2818,2249,2596,2636,2791,3010,2569,2281,3041,2957,2968,3273,2538,2424,3105,2181,2635] +                     # r = 0.1
                             [2513,2305,2040,2927,2561,2790,2396,2260,2599,3224,3035,2259,2354,3077,2785,2409,2922,2556,2803,2536]                       # r = 1
              ).astype(float)}

# modifying lambda = lambdaA + lambdaB
l_fasttree = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'MS':np.array([10395,7100,8531,9016,8846,7694,9659,9224,6890,8526,9097,7723,7332,7330,5929,5783,5351,6149,6536,6560] +       # lambda = 33.86550309051126
                            [7425,5486,7473,8311,7089,5441,5239,5851,5315,7099,7500,7711,5478,7482,6000,8083,9178,5836,6239,6058] +        # lambda = 84.66375772627816
                            [6002,5523,6755,7341,8767,5126,9399,5655,6715,7473,6666,9834,6338,5644,6227,6967,5968,8148,5411,8730] +        # lambda = 169.32751545255631
                            [9080,6796,7676,10331,7480,8986,5987,6523,7022,6365,5389,7177,6841,7359,7635,10201,6822,9349,7627,9745] +      # lambda = 338.65503090511262
                            [9017,11189,9616,10855,10075,8438,10798,11405,9295,9762,13815,9350,11550,8977,8774,9381,14896,8239,9789,11438] # lambda = 846.63757726278155
             ).astype(float)}
l_raxml    = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'MS':np.array([9525,6059,7134,9205,8497,6140,8362,7313,6457,8033,7943,6631,6855,6118,4611,5692,4917,5912,5880,6508] +        # lambda = 33.86550309051126
                            [6442,4846,6796,6838,6838,5287,4668,5229,4531,6338,6767,6538,5756,6656,4495,7265,8170,5221,4387,4391] +        # lambda = 84.66375772627816
                            [5129,4688,6231,7071,7630,4850,7777,4751,5583,6921,5921,10314,7098,5400,5934,6540,5831,7817,4656,8617] +       # lambda = 169.32751545255631
                            [8185,6675,8324,9959,7572,8703,6114,6462,6927,6955,5148,6792,6536,8066,7749,10740,7324,8394,7412,9359] +       # lambda = 338.65503090511262
                            [9067,12684,9540,9707,9921,7984,11356,11802,8990,9664,14627,9573,11688,9486,9345,9557,13977,8811,10193,11949]  # lambda = 846.63757726278155
             ).astype(float)}

# modifying sequence length
k_fasttree = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'MS':np.array([13059,11068,12225,10213,12713,16731,13832,16722,12596,12908,15296,13703,11425,14150,11582,13700,12820,15919,15232,14237] + # length = 50
                            [10814,10695,13787,9333,12179,12163,8489,11381,11001,9828,11345,15960,11595,9292,10611,10957,9261,9344,8432,8589] +         # length = 100
                            [9722,9090,8985,8271,6860,7583,9435,7534,7155,8227,8221,6828,6542,7005,7609,9577,8032,11759,10060,9237] +                   # length = 200
                            [6002,5523,6755,7341,8767,5126,9399,5655,6715,7473,6666,9834,6338,5644,6227,6967,5968,8148,5411,8730] +                     # length = 300
                            [3333,5583,4320,6009,5765,5478,4422,3443,4395,4178,5970,5068,5228,7043,5328,3767,4114,4350,5099,5164] +                     # length = 600
                            [2877,2136,3284,5239,2777,5418,4529,3278,3318,3458,3623,4970,3571,3317,3331,2999,3807,3181,2794,3917] +                     # length = 1200
                            [3639,3326,2467,1611,1661,3283,1481,1693,3850,1558,1546,1489,2792,1703,3138,3613,1491,1301,2194,1440] +                     # length = 2400
                            [1042,1734,1320,1039,1158,1354,1529,1625,1689,1628,1341,1244,1662,2292,1344,798,1538,1412,1210,2499]                        # length = 4800
             ).astype(float)}
k_raxml    = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'MS':np.array([12485,11083,11539,9757,12522,14897,13619,12605,12035,12721,15124,13203,10509,15033,12527,12441,11598,16562,14794,13682] +  # length = 50
                            [10210,10883,14036,8127,12074,11091,8630,11036,9539,10422,9415,13713,10565,9227,9898,11455,9005,8582,7245,8445] +           # length = 100
                            [9580,8649,8169,8227,6275,6837,10235,6215,7271,7737,7012,6732,5773,6737,7764,9098,7011,10899,9136,8405] +                   # length = 200
                            [5129,4688,6231,7071,7630,4850,7777,4751,5583,6921,5921,10314,7098,5400,5934,6540,5831,7817,4656,8617] +                    # length = 300
                            [3139,4827,3691,5092,5280,4063,3267,2963,4615,3997,4996,4332,4415,7820,5232,3533,3659,4355,4597,4426] +                     # length = 600
                            [1924,1951,2890,4563,2170,4613,4178,2897,2651,2719,4092,3363,2883,3077,3042,2827,2387,3279,2637,3555] +                     # length = 1200
                            [2941,3353,2512,2023,1488,2814,1748,1721,3637,1226,1423,1422,1945,1546,2667,2817,1565,1215,2155,1124] +                     # length = 2400
                            [1025,1681,1596,687,1177,1272,2022,1315,1578,1419,1285,1188,1572,1663,1243,734,929,1236,1219,1686]                          # length = 4800
             ).astype(float)}

# modifying deviation from ultrametricity
g_fasttree = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'MS':np.array([6399,7961,6215,6870,5870,6529,7352,5351,6439,7337,4874,6576,8636,5822,7899,5921,7709,6924,8185,6083] +  # gamma = 2.95181735298926
                            [8029,7473,5955,8906,7226,7233,6884,7517,7681,7397,5649,6576,6212,9894,6260,9288,9884,8430,6611,7159] +  # gamma = 5.90363470597852
                            [6002,5523,6755,7341,8767,5126,9399,5655,6715,7473,6666,9834,6338,5644,6227,6967,5968,8148,5411,8730] +  # gamma = 29.518173529892621
                            [9817,6512,4654,5679,7420,5938,6736,7223,6234,7323,5824,6398,5959,8938,6134,5969,8373,6939,8394,6151] +  # gamma = 147.590867649463
                            [5400,6532,8348,4737,5841,5896,6752,7726,6610,6651,8037,7225,6040,6832,5395,8404,6827,5098,6142,6778] +  # gamma = 295.181735298926
                            [6762,6383,7136,6539,5804,6029,4735,5952,9959,5945,4183,7511,5294,5218,7275,6723,7703,7172,6612,7390]    # gamma = infinity
             ).astype(float)}
g_raxml    = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'MS':np.array([5555,7836,6544,6529,5132,6261,7475,4777,6056,6956,4612,5538,7533,5602,7087,7132,7033,6498,6334,5744] +  # gamma = 2.95181735298926
                            [7366,6836,5907,8064,7230,6444,6410,6987,7120,6474,5839,6329,6059,8810,5992,8395,7460,6831,6969,5937] +  # gamma = 5.90363470597852
                            [5129,4688,6231,7071,7630,4850,7777,4751,5583,6921,5921,10314,7098,5400,5934,6540,5831,7817,4656,8617] + # gamma = 29.518173529892621
                            [9405,6345,4205,5817,6065,5808,6209,6200,5929,6587,4798,6590,4921,8493,5575,6565,7217,4961,6743,5220] +  # gamma = 147.590867649463
                            [5218,5109,7022,4378,5302,5446,5897,7475,5677,6758,7491,6863,5738,6240,5565,7909,6849,5009,6007,6764] +  # gamma = 295.181735298926
                            [6464,5353,6586,5898,5297,6546,4944,5997,8332,5321,4158,6517,5148,4620,7505,5915,6873,6369,5227,7081]    # gamma = infinity
             ).astype(float)}

# plot tree error (MS) vs. r (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
df = {'r':{},'MS':{},'category':{}}
for i in range(len(r_fasttree['MS'])):
    currNum = len(df['r'])
    df['r'][currNum] = r_fasttree['r'][i]
    df['MS'][currNum] = r_fasttree['MS'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['r'])
    df['r'][currNum] = r_raxml['r'][i]
    df['MS'][currNum] = r_raxml['MS'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='r',y='MS',hue='category',data=df,order=x,palette=pal)
plt.ylim(0,120000)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(E(l_b)=0.298\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (MS)',fontsize=14)
sns.plt.title(r'Tree Error (MS) vs. $\log_{10}{r}\ \left(E(l_b)=0.298\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-ms_vs_r_const-exp-branch-length.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (MS) vs. r (with constant lambda = lambdaA + lambdaB)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
df = {'r':{},'MS':{},'category':{}}
for i in range(len(r2_fasttree['MS'])):
    currNum = len(df['r'])
    df['r'][currNum] = r2_fasttree['r'][i]
    df['MS'][currNum] = r2_fasttree['MS'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['r'])
    df['r'][currNum] = r2_raxml['r'][i]
    df['MS'][currNum] = r2_raxml['MS'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='r',y='MS',hue='category',data=df,order=x,palette=pal)
plt.ylim(0,120000)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(\lambda = \lambda_A + \lambda_B = 169\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (MS)',fontsize=14)
sns.plt.title(r'Tree Error (MS) vs. $\log_{10}{r}\ \left(\lambda=\lambda_A+\lambda_B=169\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-ms_vs_r_const-lambda.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (MS) vs. lambda
fig = plt.figure()
x = np.array([33.866,84.664,169.328,338.655,846.638])
df = {'lambda':{},'MS':{},'category':{}}
for i in range(len(l_fasttree['MS'])):
    currNum = len(df['lambda'])
    df['lambda'][currNum] = l_fasttree['lambda'][i]
    df['MS'][currNum] = l_fasttree['MS'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['lambda'])
    df['lambda'][currNum] = l_raxml['lambda'][i]
    df['MS'][currNum] = l_raxml['MS'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='lambda',y='MS',hue='category',data=df,order=x,palette=pal)
plt.ylim(0,120000)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\lambda = \lambda_A + \lambda_B$',fontsize=14)
sns.plt.ylabel('Tree Error (MS)',fontsize=14)
sns.plt.title(r'Tree Error (MS) vs. $\lambda$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-ms_vs_lambda.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (MS) vs. length
fig = plt.figure()
x = np.array([50,100,200,300,600,1200,2400,4800])
df = {'length':{},'MS':{},'category':{}}
for i in range(len(k_fasttree['MS'])):
    currNum = len(df['length'])
    df['length'][currNum] = k_fasttree['length'][i]
    df['MS'][currNum] = k_fasttree['MS'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['length'])
    df['length'][currNum] = k_raxml['length'][i]
    df['MS'][currNum] = k_raxml['MS'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='length',y='MS',hue='category',data=df,order=x,palette=pal)
plt.ylim(0,120000)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel('Sequence Length',fontsize=14)
sns.plt.ylabel('Tree Error (MS)',fontsize=14)
sns.plt.title('Tree Error (MS) vs. Sequence Length',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-ms_vs_length.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (MS) vs. gamma rate
fig = plt.figure()
x = np.array([2.952,5.904,29.518,147.591,295.182,float('inf')])
df = {'gammarate':{},'MS':{},'category':{}}
for i in range(len(g_fasttree['MS'])):
    currNum = len(df['gammarate'])
    df['gammarate'][currNum] = g_fasttree['gammarate'][i]
    df['MS'][currNum] = g_fasttree['MS'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['gammarate'])
    df['gammarate'][currNum] = g_fasttree['gammarate'][i]
    df['MS'][currNum] = g_fasttree['MS'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='gammarate',y='MS',hue='category',data=df,order=x,palette=pal)
plt.ylim(0,120000)
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'Gamma Distribution Rate $\left(\alpha\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (MS)',fontsize=14)
sns.plt.title('Tree Error (MS) vs. Deviation from Ultrametricity',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-ms_vs_gammarate.pdf', format='pdf', bbox_inches='tight')
plt.close()