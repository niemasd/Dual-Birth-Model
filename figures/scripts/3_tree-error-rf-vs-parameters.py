#! /usr/bin/env python3
'''
Niema Moshiri 2016

Generate plots of Tree Error (RF) vs. various parameters
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
pal = {'simulated':'#597DBE', 'fasttree':'#C0C0C0', 'raxml':'#696969'}
#pal = {'simulated':'#597DBE', 'fasttree':'#FF0000', 'raxml':'#0000FF'}
handles = [Patch(color=pal['fasttree'],label='FastTree'),Patch(color=pal['raxml'],label='RAxML')]
axisY = np.asarray([i/10.0 for i in range(0,11,2)])

# DATASETS
# modifying r = lambdaA/lambdaB (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
r_fasttree = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'RF':np.array([0.897,0.905025,0.92072,0.905995,0.909815,0.88575,0.91898,0.90547,0.91822,0.8837,0.901105,0.93532,0.8977,0.90765,0.915855,0.91843,0.90247,0.91111,0.910415,0.8968] + # r = 0.0001
                            [0.66145,0.667,0.6911,0.6876,0.7166,0.69355,0.70735,0.69375,0.70215,0.6688,0.6801,0.7001,0.7065,0.68185,0.66885,0.7098,0.66965,0.75175,0.70865,0.68265] +            # r = 0.001
                            [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] +              # r = 0.01
                            [0.15855,0.16415,0.16615,0.18365,0.1981,0.1724,0.1644,0.1391,0.17215,0.1997,0.18295,0.17725,0.17055,0.1594,0.2023,0.18245,0.1941,0.17,0.18195,0.177] +               # r = 0.1
                            [0.102,0.1193,0.11625,0.10025,0.1028,0.13035,0.1124,0.10325,0.0782,0.0948,0.1223,0.1173,0.1114,0.12385,0.11125,0.11785,0.0995,0.1203,0.12805,0.0998]                 # r = 1
             ).astype(float)}
r_raxml    = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'RF':np.array([0.8576,0.8917,0.8887,0.8877,0.8826,0.8716,0.90271,0.8947,0.8957,0.8566,0.8816,0.91976,0.8837,0.8857,0.8927,0.8977,0.8826,0.8806,0.8756,0.8726] +                    # r = 0.0001
                            [0.6286,0.6359,0.6306,0.668,0.6901,0.674,0.663,0.659,0.651,0.6496,0.657,0.65965,0.678,0.6489,0.6419,0.682,0.6369,0.6951,0.6881,0.653] +                              # r = 0.001
                            [0.334,0.3579,0.3529,0.37695,0.3691,0.3671,0.3811,0.3661,0.34385,0.339,0.3681,0.3872,0.336,0.3691,0.335,0.38295,0.3569,0.39,0.34285,0.3619] +                        # r = 0.01
                            [0.1634,0.1594,0.1594,0.17545,0.1855,0.1674,0.1654,0.1334,0.1604,0.1895,0.17995,0.1714,0.1594,0.1554,0.2035,0.1664,0.1845,0.1654,0.1815,0.17645] +                   # r = 0.1
                            [0.09925,0.11025,0.10925,0.09725,0.10125,0.12735,0.11025,0.10125,0.0762,0.08925,0.1223,0.11425,0.10725,0.12735,0.11625,0.11025,0.0993,0.1243,0.13135,0.09525]        # r = 1
             ).astype(float)}
''' # VALUES FROM ORIGINAL RAXML TREES
r_raxml    = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'RF':np.array([0.8495,0.8957,0.8847,0.8847,0.8867,0.8676,0.8997,0.8937,0.8907,0.8536,0.8826,0.91976,0.8786,0.8857,0.8897,0.8947,0.8806,0.8816,0.8706,0.8716] +                     # r = 0.0001
                            [0.62255,0.6379,0.6256,0.662,0.674,0.655,0.6499,0.66,0.652,0.6376,0.659,0.6486,0.673,0.6429,0.6359,0.68,0.6279,0.6941,0.6851,0.6469] +                               # r = 0.001
                            [0.335,0.34185,0.3509,0.3689,0.3701,0.3661,0.3751,0.3611,0.34485,0.34,0.3541,0.3862,0.341,0.3671,0.329,0.388,0.3499,0.399,0.34685,0.3619] +                          # r = 0.01
                            [0.1704,0.1654,0.1614,0.1875,0.17645,0.1704,0.17545,0.1354,0.1644,0.1865,0.185,0.1684,0.1654,0.1544,0.2035,0.1574,0.1875,0.1724,0.1896,0.1875] +                     # r = 0.1
                            [0.10825,0.11525,0.11025,0.09825,0.10025,0.13035,0.11525,0.11125,0.0832,0.09725,0.1243,0.10425,0.10925,0.13035,0.12835,0.11225,0.1083,0.12835,0.12935,0.09725]       # r = 1
             ).astype(float)}
'''

# modifying r = lambdaA/lambdaB (with constant lambda = lambdaA + lambdaB)
r2_fasttree = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
               'RF':np.array([0.7904,0.8324,0.75215,0.7813,0.85645,0.8054,0.7884,0.7934,0.8074,0.8104,0.8195,0.7864,0.7773,0.7894,0.8023,0.7994,0.7934,0.7702,0.7573,0.8012] +              # r = 0.0001
                             [0.53135,0.56625,0.5725,0.58325,0.6014,0.57525,0.5713,0.5811,0.6106,0.62735,0.64245,0.54615,0.55945,0.5974,0.56325,0.6185,0.56005,0.58875,0.56725,0.5586] +    # r = 0.001
                             [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] +        # r = 0.01
                             [0.26925,0.28035,0.29195,0.29485,0.289,0.2834,0.2664,0.29245,0.29715,0.30455,0.28255,0.2912,0.2964,0.2895,0.3083,0.3139,0.29035,0.31225,0.28495,0.28515] +     # r = 0.1
                             [0.2575,0.25035,0.28145,0.32125,0.2951,0.30835,0.27525,0.3011,0.26855,0.2879,0.30305,0.28135,0.2904,0.31105,0.267,0.29065,0.30185,0.28325,0.28025,0.257]       # r = 1
              ).astype(float)}
r2_raxml    = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
               'RF':np.array([0.7262,0.7603,0.6861,0.7422,0.8195,0.7482,0.7161,0.7422,0.7613,0.7563,0.7462,0.7131,0.7021,0.7302,0.7823,0.7583,0.7402,0.6951,0.679,0.7392] +                 # r = 0.0001
                             [0.4895,0.5216,0.5276,0.5193,0.5557,0.51025,0.5256,0.5125,0.5496,0.5557,0.5664,0.4865,0.5226,0.5517,0.5165,0.5527,0.5085,0.5216,0.5035,0.4794] +               # r = 0.001
                             [0.334,0.3579,0.3529,0.37695,0.3691,0.3671,0.3811,0.3661,0.34385,0.339,0.3681,0.3872,0.336,0.3691,0.335,0.38295,0.3569,0.39,0.34285,0.3619] +                  # r = 0.01
                             [0.2767,0.2827,0.28675,0.29575,0.28975,0.2797,0.26465,0.28675,0.29675,0.29675,0.26565,0.28575,0.30775,0.27165,0.31375,0.31075,0.28575,0.30275,0.2817,0.2797] + # r = 0.1
                             [0.25565,0.25265,0.27065,0.34285,0.29975,0.30675,0.28375,0.31175,0.26965,0.28875,0.30675,0.28675,0.28575,0.31575,0.2827,0.30575,0.30175,0.2757,0.2817,0.26165] # r = 1
              ).astype(float)}
''' # VALUES FROM ORIGINAL RAXML TREES
r2_raxml    = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
               'RF':np.array([0.7252,0.7583,0.678,0.7392,0.8215,0.7402,0.7021,0.7432,0.7513,0.7593,0.7442,0.7172,0.7081,0.7352,0.7854,0.7543,0.7392,0.6861,0.666,0.7392] +                  # r = 0.0001
                             [0.4835,0.5145,0.5246,0.5183,0.5507,0.50525,0.5346,0.5125,0.5406,0.5537,0.5674,0.4814,0.5176,0.5496,0.5206,0.5486,0.5035,0.5176,0.5025,0.4784] +               # r = 0.001
                             [0.335,0.34185,0.3509,0.3689,0.3701,0.3661,0.3751,0.3611,0.34485,0.34,0.3541,0.3862,0.341,0.3671,0.329,0.388,0.3499,0.399,0.34685,0.3619] +                    # r = 0.01
                             [0.26965,0.28575,0.29175,0.29175,0.29475,0.27365,0.26265,0.2777,0.29075,0.29675,0.2757,0.2787,0.31275,0.27165,0.31375,0.29875,0.28775,0.3178,0.2787,0.27165] + # r = 0.1
                             [0.26465,0.25865,0.2767,0.34285,0.30675,0.30175,0.2827,0.30575,0.2767,0.28875,0.31375,0.28875,0.28375,0.30975,0.28975,0.30175,0.30175,0.2787,0.2827,0.26865]   # r = 1
              ).astype(float)}
'''

# modifying lambda = lambdaA + lambdaB
l_fasttree = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'RF':np.array([0.3631,0.318,0.32665,0.33285,0.3579,0.3499,0.342,0.33565,0.3009,0.3571,0.3089,0.3671,0.34285,0.321,0.3079,0.3159,0.2959,0.322,0.3009,0.32265] +        # lambda = 33.86550309051126
                            [0.331,0.36275,0.31375,0.338,0.3082,0.32075,0.31345,0.2801,0.33665,0.33755,0.36145,0.328,0.3285,0.334,0.31575,0.34255,0.32045,0.35755,0.325,0.3024] +   # lambda = 84.66375772627816
                            [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] + # lambda = 169.32751545255631
                            [0.525,0.5309,0.48125,0.5103,0.4868,0.51635,0.49665,0.5192,0.4519,0.49315,0.4857,0.474,0.4684,0.4994,0.4765,0.50275,0.4598,0.49255,0.49445,0.45015] +   # lambda = 338.65503090511262
                            [0.65965,0.66925,0.6423,0.64885,0.68815,0.651,0.68,0.65045,0.6474,0.69925,0.6665,0.6534,0.6322,0.6666,0.65965,0.6452,0.65705,0.65555,0.67875,0.6755]    # lambda = 846.63757726278155
             ).astype(float)}
l_raxml    = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'RF':np.array([0.336,0.2999,0.2899,0.31575,0.32585,0.3198,0.3049,0.3079,0.2909,0.344,0.3129,0.337,0.33185,0.2949,0.2738,0.3139,0.2788,0.2869,0.2869,0.335] +          # lambda = 33.86550309051126
                            [0.2929,0.342,0.2807,0.30775,0.2859,0.2827,0.2757,0.2648,0.3009,0.29175,0.317,0.3109,0.30275,0.324,0.28575,0.31475,0.29975,0.31175,0.2879,0.26465] +    # lambda = 84.66375772627816
                            [0.334,0.3579,0.3529,0.37695,0.3691,0.3671,0.3811,0.3661,0.34385,0.339,0.3681,0.3872,0.336,0.3691,0.335,0.38295,0.3569,0.39,0.34285,0.3619] +           # lambda = 169.32751545255631
                            [0.5236,0.53035,0.4822,0.48725,0.4762,0.5243,0.4774,0.5055,0.4403,0.4895,0.4744,0.45065,0.45815,0.4875,0.4684,0.48725,0.4431,0.4654,0.4814,0.45115] +   # lambda = 338.65503090511262
                            [0.65865,0.673,0.6439,0.658,0.6941,0.657,0.6931,0.65965,0.651,0.6841,0.65565,0.65815,0.6356,0.66465,0.654,0.6339,0.6379,0.651,0.68475,0.6827]           # lambda = 846.63757726278155
             ).astype(float)}
''' # VALUES FROM ORIGINAL RAXML TREES
l_raxml    = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'RF':np.array([0.336,0.2969,0.2959,0.3198,0.31575,0.3178,0.3089,0.3119,0.2989,0.348,0.3139,0.333,0.33385,0.3049,0.2758,0.3099,0.2869,0.2919,0.2859,0.344] +           # lambda = 33.86550309051126
                            [0.2989,0.348,0.28875,0.30375,0.2919,0.29075,0.2807,0.2678,0.2889,0.29475,0.322,0.32,0.30875,0.323,0.28475,0.30975,0.30275,0.31175,0.2818,0.27265] +    # lambda = 84.66375772627816
                            [0.335,0.34185,0.3509,0.3689,0.3701,0.3661,0.3751,0.3611,0.34485,0.34,0.3541,0.3862,0.341,0.3671,0.329,0.388,0.3499,0.399,0.34685,0.3619] +             # lambda = 169.32751545255631
                            [0.5155,0.5203,0.4762,0.4812,0.46315,0.5213,0.4604,0.4945,0.4323,0.4724,0.4714,0.4446,0.46215,0.4694,0.4524,0.48925,0.4311,0.4724,0.4814,0.4461] +      # lambda = 338.65503090511262
                            [0.65265,0.672,0.6389,0.652,0.6941,0.652,0.6861,0.65665,0.6449,0.681,0.6406,0.66315,0.6336,0.65465,0.6469,0.6239,0.6389,0.6449,0.6807,0.67465]          # lambda = 846.63757726278155
             ).astype(float)}
'''

# modifying sequence length
k_fasttree = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'RF':np.array([0.77405,0.7954,0.7778,0.7763,0.7989,0.78115,0.77405,0.7914,0.72955,0.7962,0.7691,0.79815,0.7902,0.77555,0.7581,0.7583,0.8095,0.7644,0.76895,0.79525] +     # length = 50
                            [0.6435,0.6201,0.64675,0.6294,0.61235,0.6452,0.65055,0.63375,0.63705,0.65075,0.6253,0.64825,0.64485,0.62945,0.67165,0.6381,0.6013,0.6241,0.61605,0.65695] + # length = 100
                            [0.4508,0.4718,0.49245,0.46975,0.45675,0.47835,0.5194,0.4673,0.4594,0.47045,0.46545,0.45465,0.4382,0.4952,0.44265,0.4987,0.49975,0.50905,0.501,0.45685] +   # length = 200
                            [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] +     # length = 300
                            [0.2457,0.24585,0.2446,0.24895,0.2743,0.25525,0.2337,0.2051,0.26905,0.24525,0.28045,0.24735,0.2508,0.26545,0.2578,0.26125,0.2223,0.2739,0.2548,0.2594] +    # length = 600
                            [0.1385,0.13835,0.1534,0.1534,0.15855,0.18105,0.1674,0.1634,0.1654,0.1846,0.1694,0.1624,0.16005,0.1671,0.16055,0.15095,0.1714,0.1595,0.1725,0.1625] +       # length = 1200
                            [0.10725,0.10825,0.1063,0.10625,0.0903,0.0943,0.0893,0.0903,0.11225,0.0903,0.0812,0.0832,0.09425,0.0953,0.08525,0.0993,0.0963,0.10425,0.1013,0.0752] +      # length = 2400
                            [0.06215,0.06015,0.0602,0.0572,0.05815,0.06015,0.0632,0.07415,0.07315,0.0461,0.0642,0.0622,0.0682,0.0682,0.0632,0.0622,0.0622,0.05515,0.06115,0.0682]       # length = 4800
             ).astype(float)}
k_raxml    = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'RF':np.array([0.78245,0.8014,0.7723,0.7549,0.7944,0.7649,0.7703,0.7864,0.74035,0.798,0.784,0.7964,0.8064,0.7914,0.7734,0.7659,0.802,0.787,0.7699,0.77595] +              # length = 50
                            [0.6309,0.5938,0.6419,0.6105,0.5998,0.6286,0.6349,0.62055,0.6399,0.6436,0.611,0.6155,0.6486,0.6105,0.651,0.6095,0.5878,0.6035,0.6058,0.6266] +              # length = 100
                            [0.4363,0.4604,0.4564,0.4491,0.4351,0.4634,0.4875,0.45015,0.4343,0.4524,0.4383,0.4323,0.4423,0.4845,0.4263,0.4694,0.4664,0.49125,0.4855,0.4351] +           # length = 200
                            [0.334,0.3579,0.3529,0.37695,0.3691,0.3671,0.3811,0.3661,0.34385,0.339,0.3681,0.3872,0.336,0.3691,0.335,0.38295,0.3569,0.39,0.34285,0.3619] +               # length = 300
                            [0.2297,0.2326,0.2297,0.2317,0.25765,0.2436,0.2165,0.2105,0.2497,0.2406,0.2528,0.2347,0.2207,0.2487,0.2407,0.2476,0.2046,0.25765,0.2367,0.2407] +           # length = 600
                            [0.1173,0.13535,0.14335,0.14935,0.13935,0.1704,0.1554,0.1574,0.1544,0.1755,0.1554,0.14735,0.1484,0.1535,0.14735,0.13935,0.1654,0.1434,0.1595,0.1454] +      # length = 1200
                            [0.09625,0.10025,0.1013,0.10825,0.0873,0.0893,0.0923,0.0873,0.11225,0.0792,0.0782,0.0792,0.08425,0.0812,0.0782,0.0943,0.0933,0.09625,0.0933,0.07015] +      # length = 2400
                            [0.06415,0.05515,0.0552,0.0512,0.05615,0.05715,0.0622,0.06415,0.06815,0.0481,0.0572,0.0582,0.0672,0.0692,0.0582,0.0582,0.0562,0.0481,0.06415,0.0612]        # length = 4800
             ).astype(float)}
''' # VALUES FROM ORIGINAL RAXML TREES
k_raxml    = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'RF':np.array([0.77845,0.8044,0.7683,0.7549,0.7954,0.7709,0.7803,0.7803,0.74735,0.796,0.786,0.7964,0.8014,0.7854,0.7704,0.7699,0.805,0.77995,0.7689,0.77595] +            # length = 50
                            [0.6279,0.5898,0.6369,0.6085,0.5988,0.62255,0.6319,0.6075,0.6379,0.6446,0.611,0.61655,0.6426,0.6145,0.651,0.6085,0.5807,0.5975,0.5988,0.61655] +            # length = 100
                            [0.4343,0.4504,0.4544,0.4381,0.4361,0.4604,0.4704,0.4431,0.4243,0.4393,0.4433,0.4293,0.4393,0.4865,0.4233,0.4684,0.4554,0.4792,0.4855,0.4301] +             # length = 200
                            [0.335,0.34185,0.3509,0.3689,0.3701,0.3661,0.3751,0.3611,0.34485,0.34,0.3541,0.3862,0.341,0.3671,0.329,0.388,0.3499,0.399,0.34685,0.3619] +                 # length = 300
                            [0.2247,0.2316,0.2377,0.2287,0.25965,0.2406,0.21755,0.2165,0.2578,0.2336,0.2367,0.2377,0.2237,0.2588,0.2518,0.2476,0.2056,0.2486,0.2427,0.2297] +           # length = 600
                            [0.13035,0.13735,0.14635,0.1564,0.14235,0.1714,0.1644,0.1644,0.1674,0.1735,0.1614,0.1584,0.1464,0.1615,0.1584,0.14035,0.1684,0.1434,0.1605,0.1464] +        # length = 1200
                            [0.10125,0.10125,0.0983,0.10925,0.0903,0.0983,0.0913,0.0923,0.11625,0.0863,0.08825,0.09025,0.09425,0.0903,0.0832,0.1013,0.1033,0.09725,0.1003,0.07415] +    # length = 2400
                            [0.06915,0.06415,0.0582,0.0572,0.05315,0.06515,0.0692,0.06715,0.0802,0.0542,0.0692,0.0672,0.0722,0.0752,0.0612,0.0622,0.0662,0.05715,0.0752,0.0692]         # length = 4800
             ).astype(float)}
'''

# modifying deviation from ultrametricity
g_fasttree = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'RF':np.array([0.41725,0.43145,0.4223,0.41265,0.4316,0.4441,0.42755,0.38405,0.41855,0.4183,0.44405,0.41245,0.4075,0.3714,0.4224,0.4,0.45145,0.4207,0.41735,0.396] +     # gamma = 2.95181735298926
                            [0.4107,0.3961,0.39445,0.39655,0.4254,0.39275,0.42315,0.4045,0.4078,0.4024,0.3673,0.39365,0.39815,0.41175,0.4014,0.45175,0.43045,0.45575,0.3931,0.4191] + # gamma = 5.90363470597852
                            [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] +   # gamma = 29.518173529892621
                            [0.3578,0.3814,0.36415,0.331,0.35295,0.41345,0.3951,0.4149,0.3967,0.3804,0.39585,0.398,0.3693,0.4057,0.3632,0.3576,0.38825,0.4029,0.38875,0.3983] +       # gamma = 147.590867649463
                            [0.3605,0.3683,0.38515,0.35425,0.39505,0.3646,0.33185,0.38665,0.39235,0.3704,0.42215,0.3831,0.3638,0.40885,0.36685,0.418,0.34975,0.35415,0.3489,0.3556] + # gamma = 295.181735298926
                            [0.4001,0.37855,0.36955,0.4024,0.37725,0.38615,0.35245,0.3933,0.3942,0.3745,0.38445,0.3762,0.39205,0.37115,0.4006,0.38395,0.38695,0.368,0.38755,0.36195]  # gamma = infinity
             ).astype(float)}
g_raxml    = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'RF':np.array([0.3831,0.4213,0.392,0.3771,0.4032,0.4132,0.4112,0.3669,0.3952,0.395,0.411,0.3771,0.37795,0.3529,0.4052,0.393,0.4112,0.4112,0.3721,0.3751] +              # gamma = 2.95181735298926
                            [0.385,0.37695,0.387,0.392,0.4032,0.3842,0.3922,0.3719,0.37895,0.3811,0.3591,0.3711,0.38345,0.3761,0.3691,0.4092,0.3872,0.4193,0.38095,0.3801] +          # gamma = 5.90363470597852
                            [0.334,0.3579,0.3529,0.37695,0.3691,0.3671,0.3811,0.3661,0.34385,0.339,0.3681,0.3872,0.336,0.3691,0.335,0.38295,0.3569,0.39,0.34285,0.3619] +             # gamma = 29.518173529892621
                            [0.339,0.3679,0.344,0.33,0.33685,0.3902,0.3709,0.3852,0.3741,0.3529,0.3639,0.3872,0.3629,0.3942,0.34,0.33085,0.3731,0.3591,0.3609,0.3601] +               # gamma = 147.590867649463
                            [0.332,0.3509,0.37595,0.32685,0.3681,0.3519,0.3228,0.3791,0.3621,0.3509,0.396,0.3629,0.3521,0.37595,0.3541,0.384,0.342,0.335,0.33585,0.33285] +           # gamma = 295.181735298926
                            [0.3842,0.3531,0.3561,0.386,0.3501,0.3709,0.3501,0.3751,0.3761,0.3711,0.3579,0.3531,0.3591,0.346,0.3831,0.3761,0.348,0.34585,0.3721,0.33285]              # gamma = infinity
             ).astype(float)}
''' # VALUES FROM ORIGINAL RAXML TREES
g_raxml    = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'RF':np.array([0.3751,0.4112,0.385,0.3912,0.3912,0.4102,0.4142,0.3539,0.3882,0.386,0.405,0.3751,0.386,0.34585,0.4042,0.39,0.4092,0.4052,0.3641,0.3671] +                # gamma = 2.95181735298926
                            [0.3749,0.3609,0.38195,0.393,0.4092,0.3761,0.3852,0.3649,0.3749,0.3831,0.3591,0.3801,0.38345,0.3701,0.3621,0.4042,0.3892,0.4183,0.37595,0.3721] +         # gamma = 5.90363470597852
                            [0.335,0.34185,0.3509,0.3689,0.3701,0.3661,0.3751,0.3611,0.34485,0.34,0.3541,0.3862,0.341,0.3671,0.329,0.388,0.3499,0.399,0.34685,0.3619] +               # gamma = 29.518173529892621
                            [0.345,0.3599,0.332,0.336,0.34285,0.3831,0.3729,0.3852,0.3641,0.3539,0.3669,0.3741,0.3549,0.3831,0.337,0.33385,0.3661,0.3601,0.3659,0.3611] +             # gamma = 147.590867649463
                            [0.326,0.33985,0.3669,0.32785,0.3651,0.34685,0.32785,0.3711,0.3671,0.33885,0.385,0.3499,0.344,0.37795,0.3631,0.3699,0.346,0.322,0.33585,0.3238] +         # gamma = 295.181735298926
                            [0.3771,0.3551,0.347,0.37995,0.3521,0.3689,0.3641,0.3561,0.3761,0.3721,0.3519,0.3571,0.3521,0.344,0.3731,0.3691,0.344,0.34885,0.3611,0.33385]             # gamma = infinity
             ).astype(float)}
'''

# modifying n
n_fasttree = {'n':np.array([25]*20+[50]*20+[250]*20+[500]*20+[1000]*20+[2000]*20+[4000]*20),
              'RF':np.array([0.2668,0.2273,0.3182,0.2727,0.4091,0.2727,0.31125,0.3636,0.3557,0.2727,0.2273,0.30195,0.2554,0.3182,0.3636,0.53465,0.0909,0.2668,0.2668,0.2273] + # n = 25
                            [0.35795,0.2553,0.28715,0.4043,0.4468,0.3723,0.1895,0.4043,0.4681,0.234,0.33685,0.20425,0.383,0.3617,0.47875,0.29025,0.3191,0.2979,0.2979,0.4574] + # n = 50
                            [0.3644,0.3971,0.3333,0.37525,0.43495,0.38365,0.417,0.3725,0.355,0.396,0.3522,0.3798,0.4028,0.3164,0.37725,0.3887,0.3482,0.34555,0.3596,0.40565] + # n = 250
                            [0.31655,0.35765,0.37375,0.3988,0.38465,0.37125,0.3605,0.3686,0.35825,0.3861,0.375,0.38935,0.38875,0.3632,0.363,0.34615,0.35985,0.39055,0.35915,0.37565] + # n = 500
                            [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] + # n = 1000
                            [0.39705,0.37135,0.38585,0.37405,0.3762,0.39125,0.37255,0.37695,0.36805,0.3823,0.36935,0.39525,0.38525,0.3937,0.38945,0.3849,0.3874,0.39455,0.37115,0.3669] + # n = 2000
                            [0.38245,0.38595,0.3826,0.3828,0.3808,0.38755,0.37725,0.3853,0.36485,0.3831,0.3657,0.3827,0.3926,0.3752,0.3854,0.4017,0.3742,0.38175,0.3673,0.3921]   # n = 4000
             ).astype(float)}
n_raxml = {'n':np.array([25]*20+[50]*20+[250]*20+[500]*20+[1000]*20+[2000]*20+[4000]*20),
              'RF':np.array([0.2668,0.3182,0.2273,0.2273,0.4091,0.3636,0.31125,0.3182,0.4002,0.2727,0.2273,0.2727,0.1818,0.3182,0.4091,0.4545,0.0455,0.2668,0.22235,0.2273] + # n = 25
                            [0.35795,0.2766,0.2948,0.3404,0.4468,0.379,0.1895,0.4468,0.3404,0.234,0.35795,0.2128,0.4043,0.3617,0.379,0.234,0.2979,0.3191,0.3191,0.35795] + # n = 50
                            [0.3563,0.3603,0.3117,0.3401,0.3684,0.3644,0.4089,0.332,0.3563,0.3919,0.3198,0.3798,0.35555,0.3111,0.3515,0.3644,0.3441,0.3482,0.38385,0.3765] + # n = 250
                            [0.2978,0.3622,0.3501,0.34175,0.35375,0.35575,0.34375,0.34375,0.3159,0.36985,0.338,0.3397,0.3779,0.33165,0.33,0.3139,0.3618,0.3561,0.32965,0.3441] + # n = 500
                            [0.335,0.34185,0.3509,0.3689,0.3701,0.3661,0.3751,0.3611,0.34485,0.34,0.3541,0.3862,0.341,0.3671,0.329,0.388,0.3499,0.399,0.34685,0.3619] + # n = 1000
                            [0.3665,0.3445,0.36195,0.3404,0.3425,0.35245,0.353,0.36095,0.36,0.35445,0.3547,0.363,0.35545,0.36875,0.366,0.3686,0.36,0.3716,0.3555,0.35095] + # n = 2000
                            [0.34975,0.36745,0.3563,0.3608,0.356,0.3531,0.3515,0.36575,0.3498,0.35575,0.33575,0.35325,0.36675,0.36,0.35325,0.37395,0.34795,0.3695,0.344,0.35795]   # n = 4000
             ).astype(float)}

# modifying model of sequence evolution
m_fasttree = {'m':['JC69']*20+['K80']*20+['HKY85']*20+['GTRCAT']*20+['GTRGAMMA']*20,
           'RF':np.array([0.3993,0.3998,0.38135,0.4216,0.426,0.3786,0.401,0.3847,0.39045,0.37825,0.3964,0.40755,0.36865,0.38565,0.3605,0.40915,0.41045,0.3978,0.37335,0.38545] + # m = JC69
                         [float('inf')]*20 + # K80
                         [float('inf')]*20 + # HKY85
                         [0.37315,0.39425,0.37025,0.3975,0.4079,0.3766,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.38055,0.34945,0.3961,0.38735,0.3968,0.3593,0.3663] + # m = GTRCAT
                         [0.37315,0.39425,0.37025,0.3995,0.4079,0.3756,0.395,0.3726,0.37335,0.35715,0.38635,0.4065,0.3545,0.37955,0.34945,0.3971,0.38635,0.3948,0.3593,0.3653] # m = GTRGAMMA
            ).astype(float)}
m_raxml = {'m':['JC69']*20+['K80']*20+['HKY85']*20+['GTRCAT']*20+['GTRGAMMA']*20,
           'RF':np.array([0.3601,0.3569,0.38195,0.391,0.4002,0.3982,0.3872,0.3651,0.3499,0.343,0.3771,0.3902,0.3571,0.3771,0.332,0.39,0.384,0.398,0.3579,0.3649] + # m = JC69
                         [0.337,0.34585,0.3569,0.3719,0.3791,0.3852,0.3852,0.3631,0.33985,0.335,0.3541,0.3962,0.337,0.3681,0.321,0.394,0.3579,0.393,0.34585,0.3649] + # m = K80
                         [0.333,0.34785,0.3609,0.3689,0.3651,0.3791,0.3922,0.3651,0.3509,0.339,0.3591,0.3882,0.347,0.3681,0.33,0.3729,0.3579,0.393,0.33485,0.3649] + # m = HKY85
                         [0.343,0.34335,0.3549,0.37895,0.3661,0.3731,0.3821,0.3631,0.33685,0.342,0.3561,0.3872,0.337,0.3621,0.33,0.38095,0.3619,0.38095,0.34185,0.3529] + # m = GTRCAT
                         [0.334,0.3579,0.3529,0.37695,0.3691,0.3671,0.3811,0.3661,0.34385,0.339,0.3681,0.3872,0.336,0.3691,0.335,0.38295,0.3569,0.39,0.34285,0.3619] # m = GTRGAMMA
            ).astype(float)}

# plot tree error (RF) vs. r (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
df = {'r':{},'RF':{},'category':{}}
for i in range(len(r_fasttree['RF'])):
    currNum = len(df['r'])
    df['r'][currNum] = r_fasttree['r'][i]
    df['RF'][currNum] = r_fasttree['RF'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['r'])
    df['r'][currNum] = r_raxml['r'][i]
    df['RF'][currNum] = r_raxml['RF'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='r',y='RF',hue='category',data=df,order=x,palette=pal)
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title(r'Tree Error (RF) vs. $\log_{10}{r}$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_r_const-exp-branch-length.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. r (with constant lambda = lambdaA + lambdaB)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
df = {'r':{},'RF':{},'category':{}}
for i in range(len(r2_fasttree['RF'])):
    currNum = len(df['r'])
    df['r'][currNum] = r2_fasttree['r'][i]
    df['RF'][currNum] = r2_fasttree['RF'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['r'])
    df['r'][currNum] = r2_raxml['r'][i]
    df['RF'][currNum] = r2_raxml['RF'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='r',y='RF',hue='category',data=df,order=x,palette=pal)
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(\lambda = \lambda_A + \lambda_B = 169\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title(r'Tree Error (RF) vs. $\log_{10}{r}\ \left(\lambda=\lambda_A+\lambda_B=169\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_r_const-lambda.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. lambda
fig = plt.figure()
x = np.array([33.866,84.664,169.328,338.655,846.638])
df = {'lambda':{},'RF':{},'category':{}}
for i in range(len(l_fasttree['RF'])):
    currNum = len(df['lambda'])
    df['lambda'][currNum] = l_fasttree['lambda'][i]
    df['RF'][currNum] = l_fasttree['RF'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['lambda'])
    df['lambda'][currNum] = l_raxml['lambda'][i]
    df['RF'][currNum] = l_raxml['RF'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='lambda',y='RF',hue='category',data=df,order=x,palette=pal)
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\lambda = \lambda_A + \lambda_B$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title(r'Tree Error (RF) vs. $\lambda$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_lambda.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. length
fig = plt.figure()
x = np.array([50,100,200,300,600,1200,2400,4800])
df = {'length':{},'RF':{},'category':{}}
for i in range(len(k_fasttree['RF'])):
    currNum = len(df['length'])
    df['length'][currNum] = k_fasttree['length'][i]
    df['RF'][currNum] = k_fasttree['RF'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['length'])
    df['length'][currNum] = k_raxml['length'][i]
    df['RF'][currNum] = k_raxml['RF'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='length',y='RF',hue='category',data=df,order=x,palette=pal)
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel('Sequence Length',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title('Tree Error (RF) vs. Sequence Length',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_length.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. gamma rate
fig = plt.figure()
x = np.array([2.952,5.904,29.518,147.591,295.182,float('inf')])
df = {'gammarate':{},'RF':{},'category':{}}
for i in range(len(g_fasttree['RF'])):
    currNum = len(df['gammarate'])
    df['gammarate'][currNum] = g_fasttree['gammarate'][i]
    df['RF'][currNum] = g_fasttree['RF'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['gammarate'])
    df['gammarate'][currNum] = g_raxml['gammarate'][i]
    df['RF'][currNum] = g_raxml['RF'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='gammarate',y='RF',hue='category',data=df,order=x,palette=pal)
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'Gamma Distribution Rate $\left(\alpha\right)$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title('Tree Error (RF) vs. Ultrametricity',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_gammarate.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. n
fig = plt.figure()
x = np.array([25,50,250,500,1000,2000,4000])
df = {'n':{},'RF':{},'category':{}}
for i in range(len(n_fasttree['RF'])):
    currNum = len(df['n'])
    df['n'][currNum] = n_fasttree['n'][i]
    df['RF'][currNum] = n_fasttree['RF'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['n'])
    df['n'][currNum] = n_raxml['n'][i]
    df['RF'][currNum] = n_raxml['RF'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='n',y='RF',hue='category',data=df,order=x,palette=pal)
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$n$',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title(r'Tree Error (RF) vs. $n$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_n.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot tree error (RF) vs. model of sequence evolution
fig = plt.figure()
df = {'m':{},'RF':{},'category':{}}
for i in range(len(m_raxml['RF'])):
    currNum = len(df['m'])
    df['m'][currNum] = m_fasttree['m'][i]
    df['RF'][currNum] = m_fasttree['RF'][i]
    df['category'][currNum] = 'fasttree'
    currNum = len(df['m'])
    df['m'][currNum] = m_raxml['m'][i]
    df['RF'][currNum] = m_raxml['RF'][i]
    df['category'][currNum] = 'raxml'
df = pd.DataFrame(df)
ax = sns.violinplot(x='m',y='RF',hue='category',data=df,palette=pal)
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel('DNA Evolution Model',fontsize=14)
sns.plt.ylabel('Tree Error (RF)',fontsize=14)
sns.plt.title(r'Tree Error (RF) vs. DNA Evolution Model',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('tree-error-rf_vs_model.pdf', format='pdf', bbox_inches='tight')
plt.close()