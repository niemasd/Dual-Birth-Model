#! /usr/bin/env python
'''
Niema Moshiri 2016

Generate plots of Cherry Deviation vs. Tree Error (RF)
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

# DATASETS
rf    = [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653,0.102,0.1193,0.11625,0.10025,0.1028,0.13035,0.1124,0.10325,0.0782,0.0948,0.1223,0.1173,0.1114,0.12385,0.11125,0.11785,0.0995,0.1203,0.12805,0.0998,0.15855,0.16415,0.16615,0.18365,0.1981,0.1724,
         0.1644,0.1391,0.17215,0.1997,0.18295,0.17725,0.17055,0.1594,0.2023,0.18245,0.1941,0.17,0.18195,0.177,0.66145,0.667,0.6911,0.6876,0.7166,0.69355,0.70735,0.69375,0.70215,0.6688,0.6801,0.7001,0.7065,0.68185,0.66885,0.7098,0.66965,0.75175,0.70865,0.68265,0.897,0.905025,0.92072,0.905995,0.909815,0.88575,0.91898,0.90547,0.91822,0.8837,0.901105,0.93532,0.8977,0.90765,
         0.915855,0.91843,0.90247,0.91111,0.910415,0.8968,0.3631,0.318,0.32665,0.33285,0.3579,0.3499,0.342,0.33565,0.3009,0.3571,0.3089,0.3671,0.34285,0.321,0.3079,0.3159,0.2959,0.322,0.3009,0.32265,0.331,0.36275,0.31375,0.338,0.3082,0.32075,0.31345,0.2801,0.33665,0.33755,0.36145,0.328,0.3285,0.334,0.31575,0.34255,0.32045,0.35755,0.325,0.3024,0.525,0.5309,
         0.48125,0.5103,0.4868,0.51635,0.49665,0.5192,0.4519,0.49315,0.4857,0.474,0.4684,0.4994,0.4765,0.50275,0.4598,0.49255,0.49445,0.45015,0.65965,0.66925,0.6423,0.64885,0.68815,0.651,0.68,0.65045,0.6474,0.69925,0.6665,0.6534,0.6322,0.6666,0.65965,0.6452,0.65705,0.65555,0.67875,0.6755,0.77405,0.7954,0.7778,0.7763,0.7989,0.78115,0.77405,0.7914,0.72955,0.7962,
         0.7691,0.79815,0.7902,0.77555,0.7581,0.7583,0.8095,0.7644,0.76895,0.79525,0.6435,0.6201,0.64675,0.6294,0.61235,0.6452,0.65055,0.63375,0.63705,0.65075,0.6253,0.64825,0.64485,0.62945,0.67165,0.6381,0.6013,0.6241,0.61605,0.65695,0.4508,0.4718,0.49245,0.46975,0.45675,0.47835,0.5194,0.4673,0.4594,0.47045,0.46545,0.45465,0.4382,0.4952,0.44265,0.4987,0.49975,0.50905,
         0.501,0.45685,0.2457,0.24585,0.2446,0.24895,0.2743,0.25525,0.2337,0.2051,0.26905,0.24525,0.28045,0.24735,0.2508,0.26545,0.2578,0.26125,0.2223,0.2739,0.2548,0.2594,0.1385,0.13835,0.1534,0.1534,0.15855,0.18105,0.1674,0.1634,0.1654,0.1846,0.1694,0.1624,0.16005,0.1671,0.16055,0.15095,0.1714,0.1595,0.1725,0.1625,0.10725,0.10825,0.1063,0.10625,0.0903,0.0943,
         0.0893,0.0903,0.11225,0.0903,0.0812,0.0832,0.09425,0.0953,0.08525,0.0993,0.0963,0.10425,0.1013,0.0752,0.06215,0.06015,0.0602,0.0572,0.05815,0.06015,0.0632,0.07415,0.07315,0.0461,0.0642,0.0622,0.0682,0.0682,0.0632,0.0622,0.0622,0.05515,0.06115,0.0682,0.41725,0.43145,0.4223,0.41265,0.4316,0.4441,0.42755,0.38405,0.41855,0.4183,0.44405,0.41245,0.4075,0.3714,
         0.4224,0.4,0.45145,0.4207,0.41735,0.396,0.4107,0.3961,0.39445,0.39655,0.4254,0.39275,0.42315,0.4045,0.4078,0.4024,0.3673,0.39365,0.39815,0.41175,0.4014,0.45175,0.43045,0.45575,0.3931,0.4191,0.3578,0.3814,0.36415,0.331,0.35295,0.41345,0.3951,0.4149,0.3967,0.3804,0.39585,0.398,0.3693,0.4057,0.3632,0.3576,0.38825,0.4029,0.38875,0.3983,0.3605,0.3683,
         0.38515,0.35425,0.39505,0.3646,0.33185,0.38665,0.39235,0.3704,0.42215,0.3831,0.3638,0.40885,0.36685,0.418,0.34975,0.35415,0.3489,0.3556,0.4001,0.37855,0.36955,0.4024,0.37725,0.38615,0.35245,0.3933,0.3942,0.3745,0.38445,0.3762,0.39205,0.37115,0.4006,0.38395,0.38695,0.368,0.38755,0.36195,0.2575,0.25035,0.28145,0.32125,0.2951,0.30835,0.27525,0.3011,0.26855,0.2879,
         0.30305,0.28135,0.2904,0.31105,0.267,0.29065,0.30185,0.28325,0.28025,0.257,0.26925,0.28035,0.29195,0.29485,0.289,0.2834,0.2664,0.29245,0.29715,0.30455,0.28255,0.2912,0.2964,0.2895,0.3083,0.3139,0.29035,0.31225,0.28495,0.28515,0.53135,0.56625,0.5725,0.58325,0.6014,0.57525,0.5713,0.5811,0.6106,0.62735,0.64245,0.54615,0.55945,0.5974,0.56325,0.6185,0.56005,0.58875,
         0.56725,0.5586,0.7904,0.8324,0.75215,0.7813,0.85645,0.8054,0.7884,0.7934,0.8074,0.8104,0.8195,0.7864,0.7773,0.7894,0.8023,0.7994,0.7934,0.7702,0.7573,0.8012]

ratio = [2.36363636364,2.24175824176,2.4,2.43181818182,2.47674418605,2.4,2.4,2.15384615385,2.25,2.09574468085,2.6,2.51724137931,2.0,2.39534883721,2.05,2.46590909091,2.40659340659,2.30769230769,2.18367346939,2.18888888889,0.984894259819,0.996932515337,0.97619047619,0.994117647059,1.0,0.981981981982,0.994202898551,0.996932515337,1.01488095238,1.00304878049,1.00313479624,0.994047619048,1.00306748466,1.0,1.0,0.975903614458,0.994029850746,1.00302114804,0.98125,1.0,1.05652173913,1.10084033613,1.08849557522,1.08154506438,1.14666666667,1.100456621,
         1.12037037037,1.08219178082,1.09777777778,1.13574660633,1.15668202765,1.07142857143,1.12107623318,1.11415525114,1.08108108108,1.14155251142,1.13615023474,1.08,1.11111111111,1.1135371179,7.90909090909,9.39285714286,10.4230769231,8.56666666667,10.48,8.96774193548,8.18181818182,9.60714285714,8.375,8.8275862069,9.92857142857,9.65517241379,10.8,9.22222222222,8.86666666667,8.83870967742,7.875,10.3703703704,10.1111111111,10.1481481481,21.4285714286,25.6666666667,45.0,30.4,32.3,25.5833333333,39.875,31.2,41.125,26.0,21.8571428571,45.1428571429,23.0769230769,35.6666666667,
         38.75,38.5,31.4,34.3333333333,33.7777777778,28.2727272727,2.44318181818,2.15909090909,2.17582417582,1.94897959184,2.27906976744,2.11111111111,2.08163265306,1.99056603774,1.96875,2.21686746988,1.88541666667,2.43373493976,2.1724137931,1.9387755102,1.86734693878,2.09473684211,2.0,1.89583333333,1.87128712871,1.97826086957,2.01030927835,2.48235294118,2.17391304348,2.33333333333,2.42857142857,2.18085106383,1.91666666667,1.94845360825,2.06818181818,2.11827956989,2.425,2.02040816327,2.01052631579,2.1978021978,1.9,2.10989010989,2.2183908046,2.29885057471,2.07777777778,1.98979591837,2.57142857143,2.50561797753,
         2.52222222222,2.70731707317,2.46808510638,2.92405063291,2.69135802469,2.52808988764,2.46739130435,2.51648351648,2.47777777778,2.24731182796,2.37894736842,2.57608695652,2.5,2.52127659574,2.49450549451,2.44444444444,2.63953488372,2.35106382979,2.64772727273,2.57303370787,2.43820224719,2.55172413793,2.52808988764,2.51724137931,2.43820224719,2.63953488372,2.61176470588,2.51724137931,2.6170212766,2.53571428571,2.80722891566,2.89411764706,2.4880952381,2.41379310345,2.6976744186,2.85714285714,2.6265060241,2.59550561798,2.57303370787,2.55319148936,2.32258064516,2.48387096774,2.125,2.54444444444,2.14141414141,2.20833333333,2.43820224719,2.53409090909,
         2.51724137931,2.69620253165,2.19791666667,2.15625,2.38947368421,2.375,2.74074074074,2.30107526882,2.77647058824,2.61538461538,2.41935483871,2.61538461538,2.60869565217,2.67032967033,2.58888888889,2.55681818182,2.32,2.80459770115,2.79775280899,2.57303370787,2.96470588235,2.4387755102,2.77011494253,2.58139534884,3.04651162791,2.64772727273,2.57954545455,2.51063829787,2.57142857143,2.81818181818,2.43023255814,2.54022988506,2.69047619048,2.42857142857,2.40217391304,2.79310344828,2.48421052632,2.55913978495,2.70731707317,2.55555555556,2.4,2.36263736264,2.42857142857,2.61797752809,2.63095238095,2.86585365854,2.52083333333,2.69411764706,
         2.55913978495,2.34736842105,1.96590909091,2.04651162791,2.02272727273,2.2375,2.03191489362,2.0,1.83333333333,1.77894736842,2.03296703297,1.9347826087,2.375,2.0,2.02222222222,1.78431372549,2.08333333333,2.0,1.81443298969,1.94444444444,2.07865168539,2.10465116279,1.64556962025,1.5,1.75,1.77173913043,1.64772727273,1.67368421053,1.64,1.59574468085,1.8488372093,1.79310344828,1.71428571429,1.70786516854,1.61,1.64444444444,1.57731958763,1.65555555556,1.64367816092,1.71276595745,1.69879518072,1.58241758242,1.55952380952,1.44086021505,1.44565217391,1.44210526316,1.37362637363,1.39772727273,
         1.45652173913,1.34408602151,1.52325581395,1.44705882353,1.34736842105,1.47777777778,1.37804878049,1.44047619048,1.36170212766,1.35353535354,1.48837209302,1.58441558442,1.37894736842,1.24210526316,1.35897435897,1.3152173913,1.18947368421,1.25287356322,1.18085106383,1.34523809524,1.27659574468,1.31818181818,1.36904761905,1.24742268041,1.3488372093,1.25301204819,1.27835051546,1.18390804598,1.33673469388,1.18556701031,1.23529411765,1.3,1.30769230769,1.3875,2.30107526882,2.38636363636,2.27472527473,2.23655913978,2.2808988764,2.55,2.3488372093,2.35164835165,2.38095238095,2.39534883721,2.25806451613,2.48913043478,2.10576923077,2.31578947368,
         2.53409090909,2.57303370787,2.30107526882,2.57142857143,2.05208333333,2.44444444444,2.47058823529,2.26086956522,2.4578313253,2.25842696629,2.54320987654,2.19587628866,2.32978723404,2.22105263158,2.27173913043,2.27083333333,2.13333333333,2.44186046512,2.37037037037,2.41176470588,2.47674418605,2.45977011494,2.23157894737,2.55681818182,2.40909090909,2.59036144578,2.2688172043,2.35294117647,2.39130434783,2.15384615385,2.16666666667,2.39024390244,2.6511627907,2.49411764706,2.91666666667,2.31868131868,2.43820224719,2.47126436782,2.20618556701,2.58974358974,2.20212765957,2.34482758621,2.37362637363,2.5,2.71052631579,2.31034482759,2.2,2.37209302326,
         2.47191011236,2.27777777778,2.34523809524,2.42528735632,2.24390243902,2.27173913043,2.34523809524,2.32954545455,2.50561797753,2.38461538462,2.37777777778,2.25263157895,2.33695652174,2.77333333333,2.25274725275,2.0404040404,2.34444444444,2.15789473684,2.3,2.44186046512,2.62025316456,2.30769230769,2.42168674699,2.41666666667,2.34482758621,2.3595505618,2.4347826087,2.24175824176,2.26804123711,2.26373626374,2.375,2.26041666667,2.44086021505,2.20618556701,2.43820224719,1.92452830189,2.44578313253,2.27906976744,0.931547619048,0.949843260188,0.903225806452,0.92899408284,0.932307692308,0.950464396285,0.935975609756,0.895061728395,0.917431192661,0.926035502959,
         0.877976190476,0.918181818182,0.952978056426,0.910714285714,0.90990990991,0.917159763314,0.867469879518,0.898203592814,0.933717579251,0.936555891239,1.15,1.125,1.15021459227,1.19111111111,1.04310344828,1.11764705882,1.0407239819,1.11659192825,1.08482142857,1.11304347826,1.07264957265,1.12385321101,1.13043478261,1.17431192661,1.16740088106,1.11894273128,1.11013215859,1.11255411255,1.17040358744,1.11415525114,6.61111111111,6.88888888889,6.61111111111,8.56666666667,9.42307692308,9.28,7.76470588235,7.46875,8.12903225806,8.4,9.34615384615,7.43333333333,7.53125,7.0303030303,6.81818181818,9.72,6.71428571429,8.41379310345,
         6.41666666667,7.125,24.3333333333,36.875,31.6666666667,30.5555555556,30.9,26.2727272727,27.8181818182,27.0,29.8,28.5,32.8888888889,27.0909090909,26.3636363636,26.0,32.3333333333,32.8888888889,42.2857142857,20.1428571429,25.1818181818,30.8888888889]

diff  = [120,113,126,126,127,126,126,105,115,103,136,132,88,120,105,129,128,119,116,107,-5,-1,-8,-2,0,-6,-2,-1,5,1,1,-2,1,0,0,-8,-2,1,-6,0,13,
         24,20,19,33,22,26,18,22,30,34,16,27,25,18,31,29,18,25,26,228,235,245,227,237,247,237,241,236,227,250,251,245,222,236,243,220,253,246,247,286,296,308,294,313,295,311,302,321,
         300,292,309,287,312,302,300,304,300,295,300,127,102,107,93,110,100,106,105,93,101,85,119,102,92,85,104,85,86,88,90,98,126,108,116,120,111,88,92,94,104,114,100,96,109,90,101,106,
         113,97,97,143,134,137,140,138,152,137,136,135,138,133,116,131,145,144,143,136,130,141,127,145,140,128,135,136,132,128,141,137,132,152,129,150,161,125,123,146,156,135,142,140,146,123,138,108,
         139,113,116,128,135,132,134,115,111,132,121,141,121,151,147,132,147,148,152,143,137,132,157,160,140,167,141,154,136,176,145,139,142,143,160,123,134,142,130,129,156,141,145,140,140,133,124,130,
         144,137,153,146,144,145,128,85,90,90,99,97,91,80,74,94,86,110,91,92,80,91,88,79,85,96,95,51,47,66,71,57,64,64,56,73,69,60,63,61,58,56,59,56,67,58,53,47,
         41,41,42,34,35,42,32,45,38,33,43,31,37,34,35,42,45,36,23,28,29,18,22,17,29,26,28,31,24,30,21,27,16,33,18,20,24,28,31,121,122,116,115,114,124,116,123,116,
         120,117,137,115,125,135,140,121,132,101,130,125,116,121,112,125,116,125,116,117,122,102,124,111,120,127,127,117,137,124,132,118,115,128,105,105,114,142,127,138,120,128,128,117,124,113,117,125,
         132,130,114,114,118,131,115,113,124,102,117,113,117,134,126,124,119,123,133,114,103,121,110,117,124,128,119,118,119,117,121,132,113,123,115,121,121,134,117,128,98,120,110,-23,-16,-33,
         -24,-22,-16,-21,-34,-27,-25,-41,-27,-15,-30,-30,-28,-44,-34,-23,-21,33,29,35,43,10,26,9,26,19,26,17,27,30,38,38,27,25,26,38,25,202,212,202,
         227,219,207,230,207,221,222,217,193,209,199,192,218,200,215,195,196,280,287,276,266,299,278,295,286,288,275,287,287,279,275,282,287,289,268,266,269]

# store data as dataframe to make it easier to work with
data = pd.DataFrame({'RF':np.asarray(rf),'ratio':np.asarray(ratio),'diff':np.asarray(diff)})

# plot cherry deviation (as difference) vs. tree error (RF)
fig = plt.figure()
sns.regplot(x='RF',y='diff',data=data)
sns.plt.xlabel('Tree Error (RF)',fontsize=14)
sns.plt.ylabel(r'Cherry Deviation $\left(Inferred-True\right)$')
sns.plt.title(r'Cherry Deviation $\left(Inferred-True\right)$ vs. Tree Error (RF)',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherry-deviation-difference_vs_tree-error-rf.png', bbox_inches='tight')
plt.close()

# plot cherry deviation (as ratio) vs. tree error (RF)
# THE DIFFERENCE PLOT LOOKS MUCH PRETTIER, SHOULD WE JUST USE THAT ONE?
fig = plt.figure()
ax = sns.regplot(x='RF',y='ratio',data=data)
sns.plt.xlabel('Tree Error (RF)',fontsize=14)
sns.plt.ylabel(r'Cherry Deviation $\left(\frac{Inferred}{True}\right)$')
sns.plt.title(r'Cherry Deviation $\left(\frac{Inferred}{True}\right)$ vs. Tree Error (RF)',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('cherry-deviation-ratio_vs_tree-error-rf.png', bbox_inches='tight')
plt.close()