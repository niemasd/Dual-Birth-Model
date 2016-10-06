#! /usr/bin/env python
'''
Niema Moshiri 2016

Generate plots of average branch length vs. various parameters
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

# Expected Branch Length as a Function of r and lambda
def exp_branch_length_vs_r_l(r,l):
    return (r+1)/(2*l*(r**0.5))

# DATASETS
# modifying r = lambdaA/lambdaB (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
r_original = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'avgbranch':np.array([0.0267173088177,0.0261440606527,0.0312439923838,0.0323414121369,0.0284412304162,0.0221902476671,0.0332732948459,0.0226990515461,0.0322243882024,0.0266119261977,0.0244588228148,0.0317945312511,0.0284623983945,0.0274336980022,0.0294185465291,0.0251340426802,0.0361775313532,0.0378493489401,0.0283413235062,0.0255517224613] + # r = 0.0001
                                   [0.0288172453829,0.0315400414579,0.0295240432778,0.0314335257526,0.0343411206552,0.0278711604309,0.0284841657065,0.0361782655956,0.0272720510435,0.0302386959695,0.0332791081614,0.0296476943958,0.0336052533775,0.0288903880247,0.0266085546863,0.0305035900252,0.0260006600931,0.0353427556564,0.0334477664964,0.0324730285238] + # r = 0.001
                                   [0.0324368929047,0.0297296903215,0.0288485932844,0.0283625675391,0.0305399759106,0.0287495336242,0.0312924089442,0.0258828176824,0.0283369150003,0.0310587031688,0.0315481480198,0.0357377345189,0.0296620093877,0.0324900928253,0.0296365747935,0.0309474224846,0.0299091439225,0.0287504569736,0.0295955130799,0.033324377919] +  # r = 0.01
                                   [0.0299481742691,0.0289619265772,0.0296858964798,0.0297792291545,0.0290083407157,0.031170217537,0.0292953427293,0.0295663785745,0.0295398968843,0.0289082105581,0.0308991197082,0.0286197107639,0.0291878001923,0.0301480809545,0.0289924890617,0.0315681614106,0.0291487309335,0.0291714524352,0.0279512663003,0.029028363695] +   # r = 0.1
                                   [0.0301758545112,0.0283734237391,0.0292391515714,0.0298961038617,0.0292665173444,0.0299198089995,0.0294413732906,0.0287958391176,0.0305076937245,0.030277653103,0.0309607757197,0.0295143582298,0.0285685168413,0.030862266786,0.0313784886087,0.0290061688089,0.0308840269252,0.02954865896,0.0290013878204,0.0314258420558]       # r = 1
             ).astype(float)}
r_inferred = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'avgbranch':np.array([0.0277010958141,0.0265143141218,0.0323989607617,0.0319814928761,0.0291314339464,0.0227122796804,0.0319834135897,0.0228791183098,0.0305442403446,0.0271591277934,0.0244915183886,0.0317114543838,0.028426164759,0.0269760587033,0.0302641240046,0.0261201045544,0.0354289151267,0.0384571628397,0.0297522129431,0.0259690047314] +  # r = 0.0001
                                   [0.0282492489113,0.0319204721501,0.0297846665391,0.0303982881751,0.0363164388012,0.0275645631831,0.0287137955639,0.0376649653051,0.0274833386826,0.0316486788842,0.0334498290035,0.0296774374243,0.0343918451152,0.0309263763241,0.0269060412675,0.0312141987748,0.0263782775323,0.0347570542275,0.0324042098405,0.0336479660488] + # r = 0.001
                                   [0.0328280374927,0.0293589119216,0.0293702403287,0.0292681320346,0.0304669867301,0.0293316668095,0.0321295772533,0.0263854120724,0.0283967136126,0.03225246587,0.0319497768996,0.0374410630995,0.0308409901689,0.0339875604079,0.0297108082644,0.0315950468596,0.0294834989233,0.028531067488,0.0302582171395,0.0339871709363] +    # r = 0.01
                                   [0.030908756487,0.0293246405779,0.0305872622326,0.0312348412715,0.0302792192364,0.0317577917227,0.0292236069209,0.0315772113499,0.0322745759664,0.0284663069264,0.0311400442172,0.0276892237524,0.0299521893201,0.0302964643453,0.0278839343805,0.0333979026186,0.0299993248823,0.0314752551242,0.0280796421003,0.0291283838921] +  # r = 0.1
                                   [0.0301889357577,0.0303062380285,0.0282059312142,0.0321063780255,0.0293023983941,0.0293900225611,0.028442782481,0.028683302495,0.0318360375896,0.0317259772173,0.0309329562267,0.030243283971,0.0291623957044,0.0319937694507,0.031138244972,0.0297647370636,0.0306398214027,0.0302573248453,0.0299996197709,0.0322849918988]       # r = 1
             ).astype(float)}

# modifying r = lambdaA/lambdaB (with constant lambda = lambdaA + lambdaB)
r2_original = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'avgbranch':np.array([0.235508623662,0.262010890762,0.26777858773,0.241735202482,0.317321260001,0.295131341426,0.231501419898,0.232604632401,0.282924404669,0.318855169806,0.275903260058,0.252841392577,0.214269304973,0.215280794679,0.299891549679,0.383802517711,0.280469785689,0.199292398496,0.197418658194,0.220236326541] +                                       # r = 0.0001
                                   [0.0771874103174,0.093522571013,0.0944345091822,0.0886075855878,0.0942926395073,0.0846837181773,0.0878442822435,0.0872843633653,0.0990605514199,0.0894565331086,0.104336800808,0.0850699683727,0.0824760998189,0.0958794515592,0.0813781099597,0.0991601749303,0.0862946707689,0.0943619042295,0.0895996381695,0.0789658810706] +                    # r = 0.001
                                   [0.0324368929047,0.0297296903215,0.0288485932844,0.0283625675391,0.0305399759106,0.0287495336242,0.0312924089442,0.0258828176824,0.0283369150003,0.0310587031688,0.0315481480198,0.0357377345189,0.0296620093877,0.0324900928253,0.0296365747935,0.0309474224846,0.0299091439225,0.0287504569736,0.0295955130799,0.033324377919] +                   # r = 0.01
                                   [0.0104230927432,0.0100345745525,0.0103151664639,0.00994326536942,0.00959895138881,0.00940962754297,0.00993734146685,0.0104469917093,0.00939680513363,0.00982917305324,0.0101244762123,0.0111928415007,0.00977384548981,0.0106629374697,0.0103899990171,0.0105269104061,0.00982281005085,0.0105245305712,0.0108628938025,0.0102633901509] +          # r = 0.1
                                   [0.00574271027405,0.00615527046848,0.00587626103644,0.00580408327046,0.00582344507897,0.0059932817163,0.00577139965317,0.0055095373957,0.00586534091989,0.00576687528432,0.00591879122331,0.005796973702,0.00596858785722,0.00607603351526,0.00590287194715,0.00594363947666,0.00590856277427,0.00575930241676,0.00588576984628,0.0063292753831]     # r = 1
             ).astype(float)}
r2_inferred = {'r':np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20), # values of r (log-scaled)
              'avgbranch':np.array([0.216102612555,0.237728725148,0.238378729585,0.220598138892,0.280139140216,0.248792812834,0.216596619703,0.214201745526,0.253509190382,0.261515098296,0.244176780691,0.224200888262,0.198881592815,0.197578800958,0.242602301057,0.301742192233,0.248085745794,0.190681480682,0.190361169683,0.202930079214] +                                      # r = 0.0001
                                   [0.0776380430566,0.0942164924424,0.0930781514727,0.0877949225338,0.0946227213793,0.0832843807231,0.0877183677064,0.0847023796321,0.0959168807181,0.088407859003,0.103102817882,0.0818617883041,0.0785649471713,0.0918447758462,0.0816049673968,0.102085071851,0.0832788748326,0.0957997004345,0.0914600294709,0.0807448356287] +                     # r = 0.001
                                   [0.0328280374927,0.0293589119216,0.0293702403287,0.0292681320346,0.0304669867301,0.0293316668095,0.0321295772533,0.0263854120724,0.0283967136126,0.03225246587,0.0319497768996,0.0374410630995,0.0308409901689,0.0339875604079,0.0297108082644,0.0315950468596,0.0294834989233,0.028531067488,0.0302582171395,0.0339871709363] +                     # r = 0.01
                                   [0.01088083443,0.00992735498489,0.0109351720587,0.0107131410991,0.0101390973401,0.00999612979154,0.0101288065317,0.010895061003,0.00987218763476,0.0105317569139,0.0102457129985,0.0120174114401,0.00970399923399,0.0110395321855,0.0107174161061,0.0106196544291,0.00976033948361,0.0102104479899,0.0111549571355,0.0106570870389] +                # r = 0.1
                                   [0.00599345508388,0.00646391016591,0.00622927652123,0.00576894738621,0.0063303263861,0.00640376569959,0.00583936552506,0.00572118207774,0.00610647881199,0.00601086128651,0.00641964555522,0.00608458938886,0.00619473873529,0.00616070627268,0.00614667713951,0.00607636779036,0.00642136849289,0.00604308441024,0.00600230603984,0.00675911011494] # r = 1
             ).astype(float)}

# modifying lambda = lambdaA + lambdaB
l_original = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'avgbranch':np.array([0.161344217969,0.13914039572,0.141880578472,0.152121461118,0.14854863721,0.153995679248,0.137604724294,0.13695170033,0.132730890029,0.15804463179,0.153967318291,0.162398566883,0.146383732671,0.135834140848,0.14213131163,0.14570627092,0.130295452985,0.142674896807,0.128650072528,0.148344543078] +                                               # lambda = 33.86550309051126
                                   [0.0575394257479,0.0565515976237,0.0655486845047,0.0602840013708,0.0634513965612,0.0578730072628,0.057906309832,0.054910833606,0.050116414039,0.0553045125509,0.0652008516828,0.0557670546682,0.0565274212505,0.0549595425016,0.0560328950153,0.0618731330533,0.0663397872985,0.059944109731,0.0526933912266,0.0532540226046] +                         # lambda = 84.66375772627816
                                   [0.0324368929047,0.0297296903215,0.0288485932844,0.0283625675391,0.0305399759106,0.0287495336242,0.0312924089442,0.0258828176824,0.0283369150003,0.0310587031688,0.0315481480198,0.0357377345189,0.0296620093877,0.0324900928253,0.0296365747935,0.0309474224846,0.0299091439225,0.0287504569736,0.0295955130799,0.033324377919] +                      # lambda = 169.32751545255631
                                   [0.0152403603366,0.014969397447,0.0159206639142,0.0174719817445,0.0155243566165,0.0159844901146,0.0144759136345,0.0134115442032,0.0142469572875,0.0149791445624,0.0130799891608,0.0152068090801,0.0138217839539,0.0144693128477,0.0144079050459,0.0149786258522,0.0145023765406,0.0142388539955,0.0144987533606,0.0140120301359] +                      # lambda = 338.65503090511262
                                   [0.00615739444225,0.00600433292579,0.00585292974031,0.00640174217878,0.00577163058783,0.00552211831022,0.00564774525726,0.00672511081415,0.00614197255059,0.00607276573989,0.00586703404507,0.00597194979227,0.00595905264059,0.00600993592936,0.00582957055436,0.00667616168129,0.00619190359535,0.00581191444748,0.005915794599,0.0061569606114]      # lambda = 846.63757726278155
             ).astype(float)} # divide by number of leaves to get percentage
l_inferred = {'lambda':np.array([33.866]*20+[84.664]*20+[169.328]*20+[338.655]*20+[846.638]*20),
              'avgbranch':np.array([0.159401676355,0.143119146848,0.13943602077,0.144122653384,0.1482882493,0.157464393554,0.135828809548,0.135581543577,0.132579478232,0.154882957309,0.156633606591,0.162897810776,0.146780818986,0.140818075046,0.145856434927,0.14167510423,0.129835103366,0.143581219252,0.125248582956,0.142577213] +                                                # lambda = 33.86550309051126
                                   [0.0604693157429,0.058339246339,0.0643995834605,0.0585328312609,0.0639507101799,0.0578836266757,0.0613798946019,0.0567041225376,0.0514580968653,0.056993765345,0.0674941721703,0.0564744919605,0.0575915933541,0.0591447873814,0.0539272253839,0.0624513646234,0.0686656067852,0.0582208754892,0.0517107301662,0.0553103145298] +                       # lambda = 84.66375772627816
                                   [0.0328280374927,0.0293589119216,0.0293702403287,0.0292681320346,0.0304669867301,0.0293316668095,0.0321295772533,0.0263854120724,0.0283967136126,0.03225246587,0.0319497768996,0.0374410630995,0.0308409901689,0.0339875604079,0.0297108082644,0.0315950468596,0.0294834989233,0.028531067488,0.0302582171395,0.0339871709363] +                        # lambda = 169.32751545255631
                                   [0.0154383765073,0.0152995890046,0.0171440767731,0.0172654187215,0.0167823620101,0.0159487654748,0.01458545532,0.0134600903485,0.01495597646,0.0148970970574,0.0128979437647,0.015907616744,0.0146244560696,0.0152191702214,0.0148568102184,0.0155448107264,0.0148786852301,0.0136708127245,0.0152917297251,0.0146697741707] +                          # lambda = 338.65503090511262
                                   [0.00665054567668,0.00700573830646,0.00607985518435,0.00689991867082,0.00580241481063,0.00574620460489,0.00568098098893,0.00735709616581,0.00677958404845,0.00628684842542,0.00651527487481,0.00625861069979,0.00627265577046,0.00642583572648,0.00618519765586,0.00682052274095,0.00657416572813,0.00595771463807,0.00619613880304,0.00624704466562]   # lambda = 846.63757726278155
             ).astype(float)}

# modifying sequence length
k_original = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'avgbranch':np.array([0.0284931012228,0.0307748834925,0.0301411062467,0.0297436066337,0.0275891512421,0.0290649108389,0.028609414352,0.0274162274925,0.0301476036583,0.0298047602971,0.0284793325808,0.029963215125,0.028837352485,0.0283873892907,0.0303243081214,0.029293205105,0.0327153929395,0.0308518385369,0.0295864403528,0.0309191005386] +    # length = 50
                                   [0.0270778195409,0.0299130834174,0.0318979519992,0.027488412488,0.0306707536898,0.029308765722,0.0270248179271,0.0320555445784,0.0290692530556,0.0284979346389,0.0304438910376,0.0285303894213,0.0304476715115,0.0296161534923,0.0298740411178,0.0302357508632,0.0299607478262,0.0312880496374,0.028793328111,0.0277394173861] +   # length = 100
                                   [0.030419808986,0.0292859000354,0.0310592580287,0.0305805704108,0.0299089491082,0.0312026029657,0.0260914805414,0.0287223750579,0.0291930395234,0.0272580200153,0.0285046210828,0.0311744982884,0.026534703066,0.0321906401393,0.0287807500189,0.0334438177267,0.0281491468137,0.0301456375809,0.0297098225001,0.0291462222521] +  # length = 200
                                   [0.0324368929047,0.0297296903215,0.0288485932844,0.0283625675391,0.0305399759106,0.0287495336242,0.0312924089442,0.0258828176824,0.0283369150003,0.0310587031688,0.0315481480198,0.0357377345189,0.0296620093877,0.0324900928253,0.0296365747935,0.0309474224846,0.0299091439225,0.0287504569736,0.0295955130799,0.033324377919] + # length = 300
                                   [0.029283946609,0.0284552208998,0.032091702207,0.0324600041667,0.0298169988045,0.0280473146183,0.0293726211966,0.0253982362318,0.0301109800056,0.0291868270968,0.0309414558942,0.0284216696536,0.0288120749584,0.0297963721996,0.031115545752,0.0302906478586,0.0291922768528,0.0289384177662,0.0318018394156,0.032831803984] +    # length = 600
                                   [0.0307311734289,0.0274205580791,0.028939800434,0.0269496451926,0.0281499320659,0.0317128459077,0.0297070788178,0.030370397764,0.0291161747811,0.0311845171899,0.0321532069617,0.0312733422706,0.0299351432161,0.0314959300496,0.0289359713235,0.0266325981277,0.0305939451407,0.0295542418277,0.0321537827674,0.031363970106] +   # length = 1200
                                   [0.0305307291262,0.030958528327,0.0271240187209,0.0263394339541,0.0293952290617,0.0294565255968,0.028540901613,0.0285658958113,0.0331315126629,0.0286675557815,0.0301055205125,0.0260360732925,0.0331989887384,0.0294023497631,0.0283741173256,0.0300299546643,0.0266228839302,0.0322598449667,0.0290677901752,0.0265800123561] +  # length = 2400
                                   [0.0360521753512,0.0311628567019,0.0285442886311,0.0308576014031,0.0295918225096,0.0284400644944,0.0287484391075,0.0285830290755,0.0336441365022,0.0252272138443,0.0274378138284,0.0302030387858,0.0276376135806,0.0290055417255,0.026796159065,0.0273370539296,0.0314225508202,0.0309531563926,0.0311517827872,0.0301353300603]   # length = 4800
             ).astype(float)}
k_inferred = {'length':np.array([50]*20+[100]*20+[200]*20+[300]*20+[600]*20+[1200]*20+[2400]*20+[4800]*20), # values of length
              'avgbranch':np.array([0.0323049922434,0.0330997329365,0.0301239618022,0.0311059176135,0.0252810806663,0.032581193386,0.0286972441282,0.0274308960005,0.0319711942442,0.02951189685,0.0289793576468,0.029861903848,0.0301088926937,0.0273234353349,0.0309292058559,0.0323661952707,0.030519146433,0.0355100152377,0.0330002379672,0.0314723987252] +     # length = 50
                                   [0.0273562202205,0.030116735938,0.0301089613672,0.0296475485859,0.0297628754723,0.0295041498544,0.0278976652915,0.0340448167358,0.0292364164156,0.0258750961136,0.0323563450516,0.0263812083153,0.029427368734,0.0277949457749,0.0306641738779,0.0328807525879,0.0312842071938,0.0308510911013,0.028681324357,0.0268408379878] +   # length = 100
                                   [0.030972220064,0.0299638091521,0.0315226136296,0.0328419410779,0.0289174589329,0.0332228654784,0.026909894458,0.0299873012441,0.0303400242964,0.0278613518415,0.0310346620186,0.0320334790433,0.028376787614,0.0309826428086,0.0292771105355,0.0344072489205,0.0296077198604,0.032635135004,0.0304579586454,0.0297026302019] +    # length = 200
                                   [0.0328280374927,0.0293589119216,0.0293702403287,0.0292681320346,0.0304669867301,0.0293316668095,0.0321295772533,0.0263854120724,0.0283967136126,0.03225246587,0.0319497768996,0.0374410630995,0.0308409901689,0.0339875604079,0.0297108082644,0.0315950468596,0.0294834989233,0.028531067488,0.0302582171395,0.0339871709363] +   # length = 300
                                   [0.0302761961251,0.0284981491874,0.0326194302566,0.0338646417916,0.0315185984637,0.0291619371572,0.030537622843,0.025583555008,0.0306140446633,0.0311873871873,0.0313634779695,0.0295955102509,0.0292493981066,0.0305070639184,0.0316019598524,0.0313036969224,0.0306495195478,0.0299053845419,0.0327121231887,0.0338669334437] +  # length = 600
                                   [0.0313626960541,0.0281599019149,0.0285180759384,0.0272499276031,0.0297688868497,0.0323819281317,0.0302250271847,0.0308701523468,0.029107307983,0.032516865492,0.0326983531076,0.0318512151351,0.03028419169,0.0325897124957,0.0295884545792,0.0269629585734,0.0306532010551,0.0305703478654,0.0327032333849,0.0319563213063] +    # length = 1200
                                   [0.0317467294715,0.0318648085465,0.0280939369515,0.0268121476897,0.0295901676171,0.0298187566306,0.0285533113283,0.0290632181982,0.033575925502,0.029423157981,0.0307882974199,0.0262049346281,0.0341295913278,0.030562281022,0.0292778882012,0.0308023171326,0.0276541889464,0.0323372589535,0.0298856928544,0.0277415727643] +   # length = 2400
                                   [0.0366509426732,0.031993037986,0.0291339746877,0.031224729494,0.0299412434915,0.0292786536767,0.0292863646101,0.0288440769319,0.0340184906201,0.0255577601877,0.0281135128078,0.0309604490235,0.0281764460836,0.0293401611922,0.0273622853488,0.0276385592467,0.0325769739675,0.0314486464885,0.031378226974,0.0305317128053]     # length = 4800
             ).astype(float)}

# modifying deviation from ultrametricity
g_original = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'avgbranch':np.array([0.0280701948074,0.0284665533238,0.0277918744686,0.0302173338564,0.0291638526198,0.0333670028798,0.0276712855466,0.0287014800751,0.0314753802416,0.0282098407188,0.0274862173473,0.0292684776963,0.0275858343415,0.0262269140665,0.0313759569632,0.0281008369503,0.0299091821043,0.0307087171474,0.0293649671045,0.0265593511075] + # gamma = 2.95181735298926
                                   [0.029280854503,0.0303339131647,0.0312736774262,0.0299482059267,0.0329865040511,0.0264479264357,0.0290350368792,0.0290737419978,0.032482052885,0.0306838854756,0.0263460558566,0.0279783333488,0.0276478216242,0.0342120186708,0.0321482342748,0.0315294191539,0.0276021969377,0.0296355229081,0.0285572878841,0.0305920085461] +   # gamma = 5.90363470597852
                                   [0.0324368929047,0.0297296903215,0.0288485932844,0.0283625675391,0.0305399759106,0.0287495336242,0.0312924089442,0.0258828176824,0.0283369150003,0.0310587031688,0.0315481480198,0.0357377345189,0.0296620093877,0.0324900928253,0.0296365747935,0.0309474224846,0.0299091439225,0.0287504569736,0.0295955130799,0.033324377919] +  # gamma = 29.518173529892621
                                   [0.0280909773791,0.0312403299266,0.0274101714725,0.0281174628637,0.0300945005087,0.0300174278269,0.0310501598931,0.0297742128717,0.0296604050025,0.0293974803834,0.028466062885,0.0294803240838,0.026384515052,0.0323299257273,0.0287017995153,0.0305639623561,0.0303971561635,0.0270553267319,0.0298093738308,0.0308214798005] +   # gamma = 147.590867649463
                                   [0.0272507080501,0.0299544786577,0.0281671481198,0.0300424858233,0.0293197091582,0.0288135325369,0.0293190994721,0.0297874992075,0.0299515392188,0.0312853943542,0.03005306282,0.0286202266779,0.0267981010643,0.0285518474584,0.0264209441491,0.032087107093,0.0301027220877,0.0266851889331,0.0321933012674,0.0281772935787] +    # gamma = 295.181735298926
                                   [0.0288622557464,0.0296434935604,0.031475222977,0.0296893563844,0.029047548373,0.0307598997306,0.0287052113716,0.0291831772636,0.0319472604556,0.0261854270557,0.0283743597612,0.0301917145229,0.0295370529574,0.028937946753,0.0316708761991,0.0302472260211,0.0328173503124,0.0263799165898,0.0321262806894,0.0297042566438]      # gamma = infinity
             ).astype(float)}
g_inferred = {'gammarate':np.array([2.952]*20+[5.904]*20+[29.518]*20+[147.591]*20+[295.182]*20+[float('inf')]*20),
              'avgbranch':np.array([0.028206649441,0.0303651699834,0.0284817734869,0.0302263967199,0.029236468005,0.0333243258302,0.0286332079733,0.0295536767143,0.0304640660407,0.0282639086702,0.0265031036492,0.0292356904905,0.0297203090723,0.0271871728198,0.03404610639,0.02795429746,0.0303843672702,0.0320602449369,0.029419008665,0.026401038837] +         # gamma = 2.95181735298926
                                   [0.0290174935979,0.0315162790807,0.0320238928419,0.0318711685814,0.0326685249709,0.0263888652307,0.0307734708114,0.0285318774847,0.0344731670787,0.0325826301175,0.0275697194955,0.0296906469147,0.0282244065113,0.0347700742343,0.0325362678624,0.0321053037008,0.0291207374935,0.0301593654603,0.0306426048251,0.0315708579283] + # gamma = 5.90363470597852
                                   [0.0328280374927,0.0293589119216,0.0293702403287,0.0292681320346,0.0304669867301,0.0293316668095,0.0321295772533,0.0263854120724,0.0283967136126,0.03225246587,0.0319497768996,0.0374410630995,0.0308409901689,0.0339875604079,0.0297108082644,0.0315950468596,0.0294834989233,0.028531067488,0.0302582171395,0.0339871709363] +    # gamma = 29.518173529892621
                                   [0.0285786823656,0.029999282585,0.0271523010872,0.0290905016772,0.030900339453,0.0313987818409,0.0309090868847,0.0291549242543,0.0304304268284,0.0297604087416,0.027762007561,0.0292458889463,0.0275966596498,0.0346690859674,0.0277324745721,0.0305942735281,0.0321898302787,0.0273355032764,0.0310148259112,0.0319091694526] +    # gamma = 147.590867649463
                                   [0.0275962998199,0.0299907045304,0.0288667218238,0.0324498326919,0.0307286897087,0.0311709246846,0.0317269768524,0.0306352181405,0.0289119169553,0.0308084702914,0.0298125478065,0.0294149525592,0.028804715643,0.0278963034323,0.028436582158,0.0326186669206,0.0299076475065,0.0268707305239,0.0326544777609,0.0288929308927] +   # gamma = 295.181735298926
                                   [0.0312357401703,0.0301406521636,0.0320185049578,0.0283382956334,0.0291644728323,0.0312038974227,0.028866041395,0.0294389286642,0.0324771578258,0.0259699268277,0.0293557383527,0.0319032626632,0.0296372389367,0.0293530949363,0.0321356588537,0.0309043840873,0.033667038491,0.0257766281958,0.0324633288627,0.0310201537093]     # gamma = infinity
             ).astype(float)}

# plot average branch length vs. r (with different lambda = lambdaA+lambdaB to keep expected branch length constant)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
df = {'r':{},'avgbranch':{},'category':{}}
for i in range(len(r_original['avgbranch'])):
    currNum = len(df['r'])
    df['r'][currNum] = r_original['r'][i]
    df['avgbranch'][currNum] = r_original['avgbranch'][i]
    df['category'][currNum] = 'original'
    currNum = len(df['r'])
    df['r'][currNum] = r_inferred['r'][i]
    df['avgbranch'][currNum] = r_inferred['avgbranch'][i]
    df['category'][currNum] = 'inferred'
df = pd.DataFrame(df)
ax = sns.violinplot(x='r',y='avgbranch',hue='category',data=df,order=x,palette='muted')
plt.plot(np.linspace(-4.5,0.5,100)+4,[0.0298238593208140]*100,label='Theoretical',linestyle='--',color='#D65F5F')
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred'),Patch(color='#D65F5F',label='Theoretical')]
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(E(l_b)=0.298\right)$',fontsize=14)
sns.plt.ylabel('Average Branch Length',fontsize=14)
sns.plt.title(r'Average Branch Length vs. $\log_{10}{r}\ \left(E(l_b)=0.298\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('avg-branch-length_vs_r_const-exp-branch-length.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot average branch length vs. r (with constant lambda = lambdaA + lambdaB)
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0])
df = {'r':{},'avgbranch':{},'category':{}}
for i in range(len(r2_original['avgbranch'])):
    currNum = len(df['r'])
    df['r'][currNum] = r2_original['r'][i]
    df['avgbranch'][currNum] = r2_original['avgbranch'][i]
    df['category'][currNum] = 'original'
    currNum = len(df['r'])
    df['r'][currNum] = r2_inferred['r'][i]
    df['avgbranch'][currNum] = r2_inferred['avgbranch'][i]
    df['category'][currNum] = 'inferred'
df = pd.DataFrame(df)
ax = sns.violinplot(x='r',y='avgbranch',hue='category',data=df,order=x,palette='muted')
x=np.linspace(-4.5,0.5,100)
plt.plot(x+4,exp_branch_length_vs_r_l(10**x,169.32751545255631),label='Theoretical',linestyle='--',color='#D65F5F')
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred'),Patch(color='#D65F5F',label='Theoretical')]
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}\ \left(\lambda = \lambda_A + \lambda_B = 169\right)$',fontsize=14)
sns.plt.ylabel('Average Branch Length',fontsize=14)
sns.plt.title(r'Average Branch Length vs. $\log_{10}{r}\ \left(\lambda=\lambda_A+\lambda_B=169\right)$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('avg-branch-length_vs_r_const-lambda.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot average branch length vs. lambda
fig = plt.figure()
x = np.array([33.866,84.664,169.328,338.655,846.638])
df = {'lambda':{},'avgbranch':{},'category':{}}
for i in range(len(l_original['avgbranch'])):
    currNum = len(df['lambda'])
    df['lambda'][currNum] = l_original['lambda'][i]
    df['avgbranch'][currNum] = l_original['avgbranch'][i]
    df['category'][currNum] = 'original'
    currNum = len(df['lambda'])
    df['lambda'][currNum] = l_inferred['lambda'][i]
    df['avgbranch'][currNum] = l_inferred['avgbranch'][i]
    df['category'][currNum] = 'inferred'
df = pd.DataFrame(df)
ax = sns.violinplot(x='lambda',y='avgbranch',hue='category',data=df,order=x,palette='muted')
sns.pointplot(x,exp_branch_length_vs_r_l(0.01,x),label='Theoretical',linestyles=['--'],color='#D65F5F')
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred'),Patch(color='#D65F5F',label='Theoretical')]
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'$\lambda = \lambda_A + \lambda_B$',fontsize=14)
sns.plt.ylabel('Average Branch Length',fontsize=14)
sns.plt.title(r'Average Branch Length vs. $\lambda$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('avg-branch-length_vs_lambda.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot average branch length vs. length
fig = plt.figure()
x = np.array([50,100,200,300,600,1200,2400,4800])
df = {'length':{},'avgbranch':{},'category':{}}
for i in range(len(k_original['avgbranch'])):
    currNum = len(df['length'])
    df['length'][currNum] = k_original['length'][i]
    df['avgbranch'][currNum] = k_original['avgbranch'][i]
    df['category'][currNum] = 'original'
    currNum = len(df['length'])
    df['length'][currNum] = k_inferred['length'][i]
    df['avgbranch'][currNum] = k_inferred['avgbranch'][i]
    df['category'][currNum] = 'inferred'
df = pd.DataFrame(df)
ax = sns.violinplot(x='length',y='avgbranch',hue='category',data=df,order=x,palette='muted')
plt.plot(np.linspace(-4.5,1000,100)+4,[0.0298238593208140]*100,label='Theoretical',linestyle='--',color='#D65F5F')
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred'),Patch(color='#D65F5F',label='Theoretical')]
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel('Sequence Length',fontsize=14)
sns.plt.ylabel('Average Branch Length',fontsize=14)
sns.plt.title('Average Branch Length vs. Sequence Length',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('avg-branch-length_vs_length.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# plot average branch length vs. gamma rate
fig = plt.figure()
x = np.array([2.952,5.904,29.518,147.591,295.182,float('inf')])
df = {'gammarate':{},'avgbranch':{},'category':{}}
for i in range(len(g_original['avgbranch'])):
    currNum = len(df['gammarate'])
    df['gammarate'][currNum] = g_original['gammarate'][i]
    df['avgbranch'][currNum] = g_original['avgbranch'][i]
    df['category'][currNum] = 'original'
    currNum = len(df['gammarate'])
    df['gammarate'][currNum] = g_inferred['gammarate'][i]
    df['avgbranch'][currNum] = g_inferred['avgbranch'][i]
    df['category'][currNum] = 'inferred'
df = pd.DataFrame(df)
ax = sns.violinplot(x='gammarate',y='avgbranch',hue='category',data=df,order=x,palette='muted')
plt.plot(np.linspace(-4.5,1000,100)+4,[0.0298238593208140]*100,label='Theoretical',linestyle='--',color='#D65F5F')
handles = [Patch(color='#597DBE',label='Original'),Patch(color='#76BF72',label='Inferred'),Patch(color='#D65F5F',label='Theoretical')]
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.plt.xlabel(r'Gamma Distribution Rate $\left(\alpha\right)$',fontsize=14)
sns.plt.ylabel('Average Branch Length',fontsize=14)
sns.plt.title('Average Branch Length vs. Deviation from Ultrametricity',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('avg-branch-length_vs_gammarate.png', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()