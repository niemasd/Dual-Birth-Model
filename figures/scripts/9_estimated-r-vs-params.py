#! /usr/bin/env python3
'''
Niema Moshiri 2016

Generate plots of inferred r vs. various parameters
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
pal = {'theoretical':'#000000', 'raxml_bl':'#62E1EA', 'raxml_cherries':'#E6C594', 'fasttree_bl_bootlier_log':'#CE8F30', 'fasttree_bl_bootlier_log_below_p25':'#00FF00', 'raxml_bl_bootlier_log':'#37ACA4'}
handles = [Patch(color=pal['theoretical'],label='Theoretical'), Patch(color=pal['raxml_cherries'],label='RAxML (Cherries)'), Patch(color=pal['raxml_bl'],label='RAxML (Branch Length)')]
axisY = np.asarray([-5,-4,-3,-2,-1,0,1])

# Expected Number of Cherries as a Function of r
def cherries_vs_r(r):
    return (r**0.5)/(1+r+r**0.5)

# Estimated r from number of cherries
def r_vs_cherries(c):
    if isinstance(c,np.ndarray):
        for i in range(len(c)):
            if c[i] > 1./3.:
                c[i] = 1./3.
    return ((1-c-((c+1)*(1-3*c))**0.5)/(2*c))**2

# set alpha transparency for axes
def setAlpha(ax,a):
    for art in ax.get_children():
        if isinstance(art, PolyCollection):
            art.set_alpha(a)

# DATASETS
# modifying r = lambdaA/lambdaB (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
r_raxml_cherries = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
                    'inferred_r':np.log10(r_vs_cherries(np.array([323,334,327,320,323,323,325,325,332,314,330,334,317,320,335,334,320,332,316,326] + # r = 0.0001
                                                                 [261,257,262,261,249,258,265,269,272,241,273,274,264,258,243,274,237,264,271,266] + # r = 0.001
                                                                 [193,190,199,193,197,196,209,190,190,199,205,218,192,199,185,197,203,203,198,189] + # r = 0.01
                                                                 [240,256,244,250,253,239,242,238,242,240,241,237,250,236,244,244,235,237,254,256] + # r = 0.1
                                                                 [329,319,327,332,348,325,343,320,338,322,317,329,323,326,329,322,335,329,312,328] + # r = 1
                                                                 [])/1000.))}
r_raxml_bl = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'inferred_r':np.log10(np.array([0.000870785,0.000721476,0.000543969,0.000812787,0.000767027,0.00115985,0.000708702,0.000788084,0.000663358,0.0008593,0.000763153,0.000542042,0.000716182,0.000671087,0.00062377,0.000828667,0.000577192,0.000572545,0.000705479,0.000833441] +# r = 0.0001
                                             [0.00218258,0.00190193,0.00115899,0.00174507,0.00140276,0.00219349,0.00252501,0.00123777,0.0019915,0.00182022,0.00169188,0.00182905,0.00125066,0.00152518,0.00239899,0.00187002,0.00240785,0.00116542,0.00154912,0.00196829] + # r = 0.001
                                             [0.0116796,0.0128327,0.0145352,0.0123368,0.0118993,0.0158731,0.00913205,0.0160686,0.0194957,0.0110458,0.00967891,0.0120827,0.0132024,0.00912984,0.0146636,0.0115625,0.0107406,0.0133031,0.014599,0.0121914] + # r = 0.01
                                             [0.152309,0.17417,0.14719,0.146065,0.128731,0.10839,0.106013,0.124227,0.130832,0.144351,0.129936,0.141635,0.106686,0.142508,0.12038,0.118949,0.093411,0.123444,0.128082,0.198322] + # r = 0.1
                                             [1,0.666462,1,0.703312,1,1,0.694874,1,1,1,1,0.627475,1,0.466592,1,0.931215,0.500904,1,0.689571,0.8059] + # r = 1
                                             []))}

# modifying r = lambdaA/lambdaB (with constant lambda = lambdaA + lambdaB)
r2_raxml_cherries = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
                    'inferred_r':np.log10(r_vs_cherries(np.array([272,261,246,264,278,248,263,273,250,258,285,259,273,255,267,260,276,243,247,257] + # r = 0.0001
                                                                 [223,220,224,239,225,226,225,222,219,238,220,214,236,218,221,223,213,218,215,210] + # r = 0.001
                                                                 [193,190,199,193,197,196,209,190,190,199,205,218,192,199,185,197,203,203,198,189] + # r = 0.01
                                                                 [243,253,260,262,249,246,253,244,250,265,252,245,255,254,253,254,247,259,252,250] + # r = 0.1
                                                                 [329,314,322,323,320,314,319,314,312,329,317,317,313,315,318,321,310,326,332,312] + # r = 1
                                                                 [])/1000.))}
r2_raxml_bl = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
                         'inferred_r':np.log10(np.array([0.00185575,0.00132657,0.00293458,0.00160861,0.00203998,0.00204604,0.00139835,0.00127956,0.00175538,0.00269108,0.00204559,0.00150601,0.00139718,0.00107835,0.00201859,0.0042152,0.00151108,0.00131407,0.000968635,0.00113553] +# r = 0.0001
                                                      [0.00221302,0.00227727,0.00172784,0.00179337,0.00150544,0.0013075,0.0024372,0.00210367,0.00166852,0.00149409,0.0015295,0.00188723,0.00234201,0.00259157,0.00214788,0.00150588,0.00224847,0.00167816,0.00192867,0.00208798] + # r = 0.001
                                                      [0.0116796,0.0128327,0.0145352,0.0123368,0.0118993,0.0158731,0.00913205,0.0160686,0.0194957,0.0110458,0.00967891,0.0120827,0.0132024,0.00912984,0.0146636,0.0115625,0.0107406,0.0133031,0.014599,0.0121914] + # r = 0.01
                                                      [0.107718,0.146927,0.142885,0.149697,0.123453,0.146388,0.138057,0.120092,0.163352,0.181324,0.117281,0.168861,0.188292,0.152836,0.111786,0.149683,0.154575,0.155888,0.133798,0.122451] + # r = 0.1
                                                      [1,1,1,1,0.668276,0.740817,0.68201,1,0.765413,1,0.53226,1,1,0.626744,0.778987,1,0.860018,0.835358,1,0.837288] + # r = 1
                                                      []
                                                      ))}

# modifying lambda = lambdaA + lambdaB
l_raxml_cherries = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
                    'inferred_r':np.log10(r_vs_cherries(np.array([200,186,190,185,183,183,194,208,190,184,180,185,182,184,177,194,170,182,181,180] + # lambda = 33.86550309051126
                                                                 [195,204,191,184,190,192,184,186,174,185,188,194,195,195,186,189,188,198,172,194] + # lambda = 84.66375772627816
                                                                 [193,190,199,193,197,196,209,190,190,199,205,218,192,199,185,197,203,203,198,189] + # lambda = 169.32751545255631
                                                                 [241,235,236,216,223,237,199,226,216,211,208,226,224,236,223,239,225,209,221,221] + # lambda = 338.65503090511262
                                                                 [270,266,263,262,286,257,267,255,263,264,266,255,256,272,260,259,256,271,263,281] + # lambda = 846.63757726278155
                                                                 [])/1000.))}
l_raxml_bl = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'inferred_r':np.log10(np.array([0.0113864,0.0145343,0.0137272,0.0170479,0.0141306,0.0141814,0.0154513,0.0169736,0.0137584,0.0109028,0.019331,0.0128141,0.0127819,0.0140409,0.0114314,0.0155412,0.011516,0.0155445,0.0165628,0.0145607] +   # lambda = 33.86550309051126
                                             [0.0113919,0.00913125,0.0107799,0.0127229,0.0115249,0.014769,0.0133383,0.0144146,0.0109348,0.0131476,0.00821475,0.0139934,0.0139321,0.0157925,0.0175885,0.0115945,0.0109861,0.010966,0.0108227,0.0148753] +  # lambda = 84.66375772627816
                                             [0.0116796,0.0128327,0.0145352,0.0123368,0.0118993,0.0158731,0.00913205,0.0160686,0.0194957,0.0110458,0.00967891,0.0120827,0.0132024,0.00912984,0.0146636,0.0115625,0.0107406,0.0133031,0.014599,0.0121914] +    # lambda = 169.32751545255631
                                             [0.0107344,0.00954578,0.0125439,0.00921421,0.0115096,0.00933032,0.0148642,0.0111706,0.0153214,0.0138004,0.0165201,0.0101954,0.0163487,0.0111589,0.0167907,0.0141905,0.0149074,0.0134243,0.0102134,0.0186013] +      # lambda = 338.65503090511262
                                             [0.0136574,0.0119322,0.0173741,0.0107716,0.0112042,0.0141499,0.0112881,0.00947459,0.0135185,0.0125378,0.0143822,0.00997774,0.0130447,0.015203,0.0137375,0.0134534,0.0115266,0.0149826,0.0146441,0.0117188]      # lambda = 846.63757726278155
                                             ))}

# modifying sequence length
k_raxml_cherries = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
                    'inferred_r':np.log10(r_vs_cherries(np.array([279,286,267,280,260,268,262,269,268,278,269,266,272,274,273,276,265,263,271,279] + # length = 50
                                                                 [255,245,257,237,240,240,254,240,252,251,259,253,243,250,256,235,250,253,253,255] + # length = 100
                                                                 [198,215,213,213,214,221,214,221,208,208,222,206,216,225,204,222,224,220,233,219] + # length = 200
                                                                 [193,190,199,193,197,196,209,190,190,199,205,218,192,199,185,197,203,203,198,189] + # length = 300
                                                                 [168,154,169,170,181,176,170,170,175,172,170,171,162,182,171,177,165,172,174,170] + # length = 600
                                                                 [140,136,143,154,147,153,166,162,153,151,141,152,154,153,152,146,150,157,140,142] + # length = 1200
                                                                 [136,135,129,138,133,128,135,128,131,128,137,137,128,125,128,138,133,118,135,128] + # length = 2400
                                                                 [112,124,114,117,118,116,126,118,125,128,121,106,130,113,128,119,113,110,129,116] + # length = 4800
                                                                 [])/1000.))}
k_raxml_bl = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'inferred_r':np.log10(np.array([0.0238124,0.0263987,0.0290364,0.028915,0.0330315,0.0256918,0.0335829,0.0354851,0.0272294,0.0299068,0.0316723,0.024782,0.0261417,0.0283754,0.0225955,0.0304431,0.0217002,0.0311585,0.0233729,0.0275233] +  # length = 50
                                             [0.0185514,0.0193585,0.0117487,0.0156878,0.0170298,0.0182602,0.0151984,0.0168458,0.0141487,0.0181164,0.0146396,0.0183307,0.0170749,0.0180811,0.0110642,0.0184674,0.0167497,0.0178668,0.0156366,0.0168387] +   # length = 100
                                             [0.0100744,0.0133927,0.0141384,0.0147626,0.0143518,0.0105631,0.0117754,0.0145847,0.0124883,0.0175475,0.0138732,0.0132588,0.0176813,0.0129866,0.0114365,0.0116927,0.0181756,0.0102249,0.0116411,0.014984] +   # length = 200
                                             [0.0116796,0.0128327,0.0145352,0.0123368,0.0118993,0.0158731,0.00913205,0.0160686,0.0194957,0.0110458,0.00967891,0.0120827,0.0132024,0.00912984,0.0146636,0.0115625,0.0107406,0.0133031,0.014599,0.0121914] +    # length = 300
                                             [0.00853671,0.00865184,0.0094752,0.00841453,0.0144865,0.0105462,0.0147194,0.0166405,0.0101532,0.0142705,0.00989013,0.00948399,0.013364,0.0168005,0.009981,0.0110714,0.0162591,0.0115048,0.00966015,0.0089585] + # length = 600
                                             [0.0094413,0.00991061,0.0121278,0.0129669,0.00943164,0.0127004,0.0122888,0.0118003,0.0122739,0.0102148,0.00983116,0.00938313,0.0148654,0.0105713,0.0162827,0.0108938,0.0104154,0.0135422,0.010089,0.0137002] +  # length = 1200
                                             [0.00832997,0.0130088,0.0114084,0.0141906,0.00921681,0.0101034,0.0113182,0.0121352,0.0103804,0.0093393,0.0105383,0.0109388,0.00854012,0.00830718,0.0115082,0.00966318,0.0094308,0.00642568,0.0116843,0.0121424] + # length = 2400
                                             [0.00762159,0.0113809,0.0147904,0.00794803,0.0132574,0.00978842,0.0137171,0.0105242,0.00857839,0.011209,0.00799564,0.0110234,0.0123555,0.00880314,0.0134024,0.0125546,0.00863298,0.00755903,0.0115519,0.00903266]    # length = 4800
                                             ))}

# modifying deviation from ultrametricity
g_raxml_cherries = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
                    'inferred_r':np.log10(r_vs_cherries(np.array([212,196,204,200,202,196,199,205,194,205,202,215,206,203,213,207,218,206,194,193] + # gamma = 2.95181735298926
                                                                 [199,195,189,202,211,214,202,206,195,212,191,198,188,190,202,205,209,208,198,202] + # gamma = 5.90363470597852
                                                                 [193,190,199,193,197,196,209,190,190,199,205,218,192,199,185,197,203,203,198,189] + # gamma = 29.518173529892621
                                                                 [196,188,205,196,187,188,203,198,190,211,217,207,211,189,195,192,203,195,185,189] + # gamma = 147.590867649463
                                                                 [189,187,210,203,184,188,184,203,179,193,211,196,195,202,203,197,200,191,192,203] + # gamma = 295.181735298926
                                                                 [208,201,197,209,194,202,194,193,209,193,208,189,191,203,209,192,196,185,194,186] + # gamma = infinity
                                                                 [])/1000.))}
g_raxml_bl = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'inferred_r':np.log10(np.array([0.00942352,0.00833048,0.0108756,0.0143512,0.0117049,0.0106471,0.012181,0.0116684,0.00995295,0.00963702,0.0157126,0.00987403,0.0156713,0.014367,0.0151278,0.0119494,0.0109711,0.0126528,0.0168896,0.0179312] +    # gamma = 2.95181735298926
                                             [0.012748,0.0125605,0.0136604,0.0128767,0.011879,0.0196796,0.0108641,0.0138477,0.0110647,0.0110084,0.0127802,0.00861143,0.0107866,0.00890205,0.0137482,0.0104897,0.0103873,0.0147223,0.0113472,0.0112625] +  # gamma = 5.90363470597852
                                             [0.0116796,0.0128327,0.0145352,0.0123368,0.0118993,0.0158731,0.00913205,0.0160686,0.0194957,0.0110458,0.00967891,0.0120827,0.0132024,0.00912984,0.0146636,0.0115625,0.0107406,0.0133031,0.014599,0.0121914] +    # gamma = 29.518173529892621
                                             [0.014589,0.0103896,0.0127874,0.0137691,0.0130813,0.010088,0.0110471,0.0114526,0.00802045,0.0111899,0.0115302,0.0113448,0.0140263,0.00840114,0.0136352,0.00937374,0.0117375,0.0119783,0.00842957,0.0112472] +   # gamma = 147.590867649463
                                             [0.0143025,0.0116274,0.0124971,0.0133305,0.00938278,0.0167998,0.0110728,0.0132797,0.0118169,0.013594,0.0113459,0.013195,0.0120778,0.0115385,0.0139171,0.00876632,0.0103641,0.0137551,0.0118614,0.0137252] +        # gamma = 295.181735298926
                                             [0.0122184,0.00903168,0.00893515,0.0128871,0.0123187,0.0111515,0.0101066,0.01087,0.0151499,0.0115506,0.0135429,0.0163078,0.0124123,0.0113076,0.0107022,0.0175676,0.00945462,0.0163576,0.0117161,0.0125759]        # gamma = infinity
                                             ))}

# modifying n
n_raxml_cherries = {'n':np.array([25]*20+[50]*20+[250]*20+[500]*20+[1000]*20+[2000]*20+[4000]*20),
                    'inferred_r':np.log10(r_vs_cherries(np.array([0.24,0.16,0.12,0.16,0.24,0.2,0.16,0.2,0.16,0.24,0.2,0.12,0.24,0.16,0.2,0.2,0.12,0.2,0.12,0.2] + # n = 25
                                                                 [0.18,0.2,0.2,0.2,0.22,0.16,0.16,0.3,0.18,0.16,0.24,0.22,0.2,0.18,0.18,0.14,0.2,0.22,0.16,0.22] + # n = 50
                                                                 [0.204,0.184,0.188,0.212,0.188,0.212,0.196,0.184,0.2,0.216,0.192,0.188,0.212,0.18,0.188,0.208,0.18,0.188,0.212,0.192] + # n = 250
                                                                 [0.19,0.21,0.194,0.202,0.198,0.19,0.2,0.208,0.182,0.224,0.188,0.216,0.204,0.218,0.212,0.186,0.192,0.194,0.198,0.192] + # n = 500
                                                                 [0.193,0.19,0.199,0.193,0.197,0.196,0.209,0.19,0.19,0.199,0.205,0.218,0.192,0.199,0.185,0.197,0.203,0.203,0.198,0.189] + # n = 1000
                                                                 [0.199,0.2075,0.1935,0.199,0.19,0.188,0.194,0.2,0.2,0.196,0.197,0.204,0.1955,0.196,0.2075,0.1985,0.192,0.2035,0.201,0.1955] + # n = 2000
                                                                 [0.199,0.20525,0.2005,0.20475,0.19325,0.1915,0.201,0.2,0.19425,0.195,0.1865,0.1965,0.20375,0.19575,0.2,0.20025,0.19,0.199,0.1895,0.19925] + # n = 4000
                                                                 [])))}
n_raxml_bl = {'n':np.array([25]*20+[50]*20+[250]*20+[500]*20+[1000]*20+[2000]*20+[4000]*20),
              'inferred_r':np.log10(np.array([0.163654826882608,0.019668103943059,0.0113511292241568,0.02482024815094,0.00889055626266301,0.0129092084454817,0.0171662181066667,0.00907853590054184,0.015277424026425,0.0132110958938845,0.010374821601061,0.0174385738966955,0.0478710608079377,0.0124704146318607,0.0216622381660909,0.00632467536089941,0.0193141140410937,0.0189439363962626,0.0186816721797017,0.0293088430978665] + # n = 25
                                             [0.00687872976990467,0.0147949265431412,0.0299487020040268,0.0419551198359811,0.00420313803034544,0.00842389759953178,0.0235681890503354,0.013831698936855,0.0139817008490749,0.0166627719973719,0.0244174811272832,0.0263155654761482,0.00857209465609564,0.0118744510392997,0.00460301906874792,0.0257933133950226,0.0115268815431111,0.0112992397725408,0.0227634286082296,0.00887416329971246] + # n = 50
                                             [0.0200310271440538,0.0113187215433581,0.0158882510665668,0.0092022137241614,0.0150286296385417,0.0116135003841824,0.00924057672696924,0.0110124436229106,0.009847812152829,0.0131580271920457,0.019780052584658,0.0156741731663439,0.0157639327196692,0.0281595355644211,0.0134685125376008,0.0144068685177803,0.00943748950315644,0.0144357741728012,0.0398114828556822,0.0124303212624557] +    # n = 250
                                             [0.0163974310918051,0.0120062799536374,0.0127573683182669,0.0227579647716562,0.0106864415744574,0.0118779546485216,0.0159481924969736,0.0133704657375816,0.0169486082871304,0.0118621755372802,0.0132855475568465,0.0089763242110216,0.0139704807791852,0.0138526955190169,0.0133820302906149,0.0131127289041883,0.0170559624771676,0.00961937786082379,0.0200579911537235,0.00876507149013026] +  # n = 500
                                             [0.0116795977659254,0.012832669983785,0.0145351725846893,0.0123368327278828,0.0118992558449749,0.0158730875691259,0.00913205415625011,0.0160686329330372,0.0194957264695963,0.011045804008226,0.00967890687641233,0.0120826533539407,0.0132024119181044,0.00912984013629388,0.0146636208142731,0.0115625041123262,0.010740599099085,0.0133031463973541,0.0145989991093193,0.0121914339574952] +    # n = 1000
                                             [0.0118200295537734,0.0113773172884364,0.01300475884468,0.0131796415638609,0.011014870024938,0.0101340095653411,0.0141675296856298,0.0122865188449237,0.0179009378596262,0.0123142801117646,0.0105359462222185,0.0109875212706925,0.0131814426236468,0.0105615428347608,0.0148783580741809,0.0115433608903395,0.00904694361519916,0.0137387101432555,0.0124991031657156,0.0173270351020304] +   # n = 2000
                                             [0.0130500312835607,0.0116756358215603,0.012962856737449,0.0127949347457197,0.0127106933396624,0.0115322562707222,0.0128885461077385,0.0118681636899749,0.014098482713256,0.011301175913231,0.0139257703790647,0.0153433123024074,0.011727416898757,0.013846985736737,0.0130411544893496,0.0121364398677197,0.013983894710098,0.0148495584919366,0.0142699666697717,0.0124304608670564]        # n = 4000
                                             ))}

# plot Estimated $\log_{10}{r}$ vs. r (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
ax = sns.violinplot(x='r',y='inferred_r',data=pd.DataFrame(r_raxml_bl),order=x,color=pal['raxml_bl'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([sum(r_raxml_bl['r'][i:i+20])/20.0 for i in range(0,len(r_raxml_bl['inferred_r']),20)])+4,[sum(r_raxml_bl['inferred_r'][i:i+20])/20.0 for i in range(0,len(r_raxml_bl['inferred_r']),20)],color=pal['raxml_bl'],linestyle=':',linewidth=3)
sns.violinplot(x='r',y='inferred_r',data=pd.DataFrame(r_raxml_cherries),order=x,color=pal['raxml_cherries'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([sum(r_raxml_cherries['r'][i:i+20])/20.0 for i in range(0,len(r_raxml_cherries['inferred_r']),20)])+4,[sum(r_raxml_cherries['inferred_r'][i:i+20])/20.0 for i in range(0,len(r_raxml_cherries['inferred_r']),20)],color=pal['raxml_cherries'],linestyle=':',linewidth=3)
setAlpha(ax,0.5)
plt.plot([-1,0,1,2,3,4,5],[-5,-4,-3,-2,-1,0,1],label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(E(l_b)=0.298\right)$',fontsize=14)
sns.plt.ylabel(r'Estimated $\log_{10}{r}$',fontsize=14)
sns.plt.title(r'Estimated $\log_{10}{r}$ vs. $\log_{10}{r}\ \left(E(l_b)=0.298\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('estimated-r_vs_r_const-exp-branch-length_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Estimated $\log_{10}{r}$ vs. r (with constant lambda = lambdaA + lambdaB)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
ax = sns.violinplot(x='r',y='inferred_r',data=pd.DataFrame(r2_raxml_bl),order=x,color=pal['raxml_bl'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([sum(r2_raxml_bl['r'][i:i+20])/20.0 for i in range(0,len(r2_raxml_bl['inferred_r']),20)])+4,[sum(r2_raxml_bl['inferred_r'][i:i+20])/20.0 for i in range(0,len(r2_raxml_bl['inferred_r']),20)],color=pal['raxml_bl'],linestyle=':',linewidth=3)
sns.violinplot(x='r',y='inferred_r',data=pd.DataFrame(r2_raxml_cherries),order=x,color=pal['raxml_cherries'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([sum(r2_raxml_cherries['r'][i:i+20])/20.0 for i in range(0,len(r2_raxml_cherries['inferred_r']),20)])+4,[sum(r2_raxml_cherries['inferred_r'][i:i+20])/20.0 for i in range(0,len(r2_raxml_cherries['inferred_r']),20)],color=pal['raxml_cherries'],linestyle=':',linewidth=3)
setAlpha(ax,0.5)
x = np.linspace(-4,0,100)
plt.plot([-1,0,1,2,3,4,5],[-5,-4,-3,-2,-1,0,1],label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(\lambda = \lambda_A + \lambda_B = 169\right)$',fontsize=14)
sns.plt.ylabel(r'Estimated $\log_{10}{r}$',fontsize=14)
sns.plt.title(r'Estimated $\log_{10}{r}$ vs. $\log_{10}{r}\ \left(\lambda=\lambda_A+\lambda_B=169\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('estimated-r_vs_r_const-lambda_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Estimated $\log_{10}{r}$ vs. lambda
fig = plt.figure()
x = np.array([33.866,84.664,169.328,338.655,846.638])
ax = sns.violinplot(x='lambda',y='inferred_r',data=pd.DataFrame(l_raxml_bl),order=x,color=pal['raxml_bl'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([int(i/20) for i in range(0,len(l_raxml_bl['inferred_r']),20)]),[sum(l_raxml_bl['inferred_r'][i:i+20])/20.0 for i in range(0,len(l_raxml_bl['inferred_r']),20)],color=pal['raxml_bl'],linestyle=':',linewidth=3)
sns.violinplot(x='lambda',y='inferred_r',data=pd.DataFrame(l_raxml_cherries),order=x,color=pal['raxml_cherries'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([int(i/20) for i in range(0,len(l_raxml_cherries['inferred_r']),20)]),[sum(l_raxml_cherries['inferred_r'][i:i+20])/20.0 for i in range(0,len(l_raxml_cherries['inferred_r']),20)],color=pal['raxml_cherries'],linestyle=':',linewidth=3)
setAlpha(ax,0.5)
x = np.linspace(-100,1000,1100)
plt.plot([-10,10],[-2,-2],label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\lambda = \lambda_A + \lambda_B$',fontsize=14)
sns.plt.ylabel(r'Estimated $\log_{10}{r}$',fontsize=14)
sns.plt.title(r'Estimated $\log_{10}{r}$ vs. $\lambda$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('estimated-r_vs_lambda_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Estimated $\log_{10}{r}$ vs. length
fig = plt.figure()
x = np.array([50,100,200,300,600,1200,2400,4800])
ax = sns.violinplot(x='length',y='inferred_r',data=pd.DataFrame(k_raxml_bl),order=x,color=pal['raxml_bl'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([int(i/20) for i in range(0,len(k_raxml_bl['inferred_r']),20)]),[sum(k_raxml_bl['inferred_r'][i:i+20])/20.0 for i in range(0,len(k_raxml_bl['inferred_r']),20)],color=pal['raxml_bl'],linestyle=':',linewidth=3)
sns.violinplot(x='length',y='inferred_r',data=pd.DataFrame(k_raxml_cherries),order=x,color=pal['raxml_cherries'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([int(i/20) for i in range(0,len(k_raxml_cherries['inferred_r']),20)]),[sum(k_raxml_cherries['inferred_r'][i:i+20])/20.0 for i in range(0,len(k_raxml_cherries['inferred_r']),20)],color=pal['raxml_cherries'],linestyle=':',linewidth=3)
setAlpha(ax,0.5)
plt.plot([-10,10],[-2,-2],label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel('Sequence Length',fontsize=14)
sns.plt.ylabel(r'Estimated $\log_{10}{r}$',fontsize=14)
sns.plt.title('Estimated $\log_{10}{r}$ vs. Sequence Length',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('estimated-r_vs_length_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Estimated $\log_{10}{r}$ vs. gamma rate
fig = plt.figure()
x = np.array([2.952,5.904,29.518,147.591,295.182,float('inf')])
ax = sns.violinplot(x='gammarate',y='inferred_r',data=pd.DataFrame(g_raxml_bl),order=x,color=pal['raxml_bl'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([int(i/20) for i in range(0,len(g_raxml_bl['inferred_r']),20)]),[sum(g_raxml_bl['inferred_r'][i:i+20])/20.0 for i in range(0,len(g_raxml_bl['inferred_r']),20)],color=pal['raxml_bl'],linestyle=':',linewidth=3)
sns.violinplot(x='gammarate',y='inferred_r',data=pd.DataFrame(g_raxml_cherries),order=x,color=pal['raxml_cherries'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([int(i/20) for i in range(0,len(g_raxml_cherries['inferred_r']),20)]),[sum(g_raxml_cherries['inferred_r'][i:i+20])/20.0 for i in range(0,len(g_raxml_cherries['inferred_r']),20)],color=pal['raxml_cherries'],linestyle=':',linewidth=3)
setAlpha(ax,0.5)
plt.plot([-10,10],[-2,-2],label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'Gamma Distribution Rate $\left(\alpha\right)$',fontsize=14)
sns.plt.ylabel(r'Estimated $\log_{10}{r}$',fontsize=14)
sns.plt.title('Estimated $\log_{10}{r}$ vs. Deviation from Ultrametricity',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('estimated-r_vs_gammarate_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot Estimated $\log_{10}{r}$ vs. n
fig = plt.figure()
x = np.array([250,500,1000,2000,4000])
ax = sns.violinplot(x='n',y='inferred_r',data=pd.DataFrame(n_raxml_bl),order=x,color=pal['raxml_bl'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([int(i/20) for i in range(0,len(n_raxml_bl['inferred_r']),20)]),[sum(n_raxml_bl['inferred_r'][i:i+20])/20.0 for i in range(0,len(n_raxml_bl['inferred_r']),20)],color=pal['raxml_bl'],linestyle=':',linewidth=3)
sns.violinplot(x='n',y='inferred_r',data=pd.DataFrame(n_raxml_cherries),order=x,color=pal['raxml_cherries'],scale='width',width=0.3,inner=None)
plt.plot(np.asarray([int(i/20) for i in range(0,len(n_raxml_cherries['inferred_r']),20)]),[sum(n_raxml_cherries['inferred_r'][i:i+20])/20.0 for i in range(0,len(n_raxml_cherries['inferred_r']),20)],color=pal['raxml_cherries'],linestyle=':',linewidth=3)
setAlpha(ax,0.5)
plt.plot([-10,10],[-2,-2],label='Theoretical',linestyle='--',color=pal['theoretical'])
plt.yticks(axisY); plt.ylim(axisY[0],axisY[-1])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$n$',fontsize=14)
sns.plt.ylabel(r'Estimated $\log_{10}{r}$',fontsize=14)
sns.plt.title('Estimated $\log_{10}{r}$ vs. $n$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('estimated-r_vs_n_with-corrections.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()