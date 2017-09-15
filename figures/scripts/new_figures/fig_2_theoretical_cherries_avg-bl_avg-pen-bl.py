#! /usr/bin/env python3
'''
Niema Moshiri 2016

Generate plots of theoretical cherries and average branch length and pendant
branch length with simulated values.
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
LAMBDA = 84.
sns.set_style("ticks")
rcParams['font.family'] = 'serif'
pal = {'cherries':'#FF0000', 'avg_bl':'#0000FF', 'avg_pen_bl':'#00FF00'}

# Expected Number of Cherries as a Function of r
def cherries_vs_r(r):
    return (r**0.5)/(1+r+r**0.5)

# Expected Average Branch Length as a Function of r
def avg_bl_vs_r(r):
    return ((r+1)/(r**0.5))/(2*LAMBDA)

# Expected Average Pendant Branch Length as a Function of r
def avg_pen_bl_vs_r(r):
    r_fix = np.array([i if i <= 1 else 1./i for i in r])
    return ((r_fix**0.5)/(1+2*(r_fix**0.5)-r_fix))/((LAMBDA*r_fix)/(r_fix+1))

data = {'r':  np.array([-4]*20+[-3]*20+[-2]*20+[-1]*20+[0]*20+[1]*20+[2]*20+[3]*20+[4]*20),
   'avg_bl':  np.array([0.533662141598045,0.515851558151391,0.419996640683004,0.488206470821705,0.571099801406938,0.673436078398145,0.454704635334637,0.66496331006593,0.684540129685004,0.466559593046599,0.641287620158894,0.569121575826864,0.584144349199816,0.517508568032524,0.582112199520797,0.421069047623693,0.544480346261341,0.52935130485105,0.660790356170134,0.425481182230542] +
                       [0.190206053166292,0.175079154543219,0.162194704699472,0.192847837839863,0.177362312796898,0.205647046303615,0.175599672405481,0.176448852355086,0.198927398461847,0.191522256440938,0.1629633324347,0.149098174256849,0.180371147328315,0.194779912725012,0.158840134120757,0.180040690248666,0.176345691135369,0.228960096991436,0.198619704498578,0.182589826134973] +
                       [0.0572346650363703,0.0642585808095261,0.0548284370388808,0.0598740210250611,0.057696952408549,0.0533924618499217,0.0652233671317537,0.0610559759395212,0.0544609215428775,0.0605498927660968,0.0571968958628286,0.0627594041024768,0.0607933728933074,0.0634556583136786,0.0624080029080165,0.0572433484582706,0.0555106107334442,0.0564036410349097,0.059676770507704,0.057863389851071] +
                       [0.0208019488167807,0.020705419196594,0.0207728142412799,0.0208256055334977,0.0202662377552516,0.0187790715765999,0.0201435046482413,0.0196907866715486,0.0212630911494969,0.0208027755090327,0.0200181032070933,0.02175403220298,0.0200692776427406,0.0219251073956814,0.0199268448176404,0.0212318836344894,0.0210245867203713,0.0197556420377137,0.0200730053630679,0.0208176215177186] +
                       [0.0122655472030386,0.0115332045823058,0.0122114897308842,0.0120536932825305,0.0120909031619394,0.0117984870161944,0.0113330008289546,0.0125246907345676,0.012011130107616,0.0121714733660381,0.0116987079454714,0.011397233400143,0.0112874898488031,0.0109563031913532,0.011712179913786,0.0120816084729555,0.011593693596893,0.0116126708234489,0.0118548588213483,0.0119087549507425] +
                       [0.0210387482422716,0.0206327641749488,0.0199461912214314,0.0202689755150978,0.0202001416124963,0.0204686376341524,0.0212288846064192,0.0199144766519297,0.0208151108815926,0.0205181663661407,0.0201501486395896,0.0198006831131803,0.0214152594286029,0.0205863373193478,0.0194418050226674,0.0221804890521739,0.0207104584473864,0.0208054926114802,0.0210968761146361,0.0191469899332682] +
                       [0.053402513513869,0.0666300706939228,0.0637107078990231,0.0596095422537909,0.0629918075577774,0.0601719819708795,0.0511690673029801,0.0552559007475623,0.0634748631790424,0.0572571775266732,0.0600946240408988,0.058289410576937,0.0618331841141672,0.0629371764152712,0.0679375095830971,0.0622811069545236,0.0596168705801367,0.0638038684844502,0.0606868848454372,0.0597073105855351] +
                       [0.168902589992081,0.194490480703527,0.171645054246312,0.162995566650874,0.217876975456014,0.170016288864533,0.170058127420753,0.18438877048729,0.197924445211212,0.155716195645139,0.181435210871324,0.17712359498894,0.233311944617249,0.204169935967333,0.159380194239762,0.203419635061456,0.185037048254177,0.166457264937811,0.177169609324093,0.206302665659091] +
                       [0.70707648789445,0.482301501936268,0.61330793329282,0.786058849974352,0.611614123388912,0.566335043791305,0.71261236108486,0.486423810216512,0.610954290010118,0.720381954501595,0.527290185728054,0.647016189303375,0.474677633128334,0.452457532919278,0.751201174429573,0.77140791594921,0.46600472411276,0.607314897812887,0.504618441067238,0.495232210128129]),
'avg_pen_bl': np.array([0.893789648808594,0.94555131286914,1.07761794485352,1.36489726236914,0.970191562267578,1.14556579264063,1.21096343993359,1.05161498114258,1.34596628200781,1.06706198671172,0.909228384873046,1.01929747512695,1.13092940498633,1.1059187359082,1.01886346824219,1.05082763438476,0.998905750951172,1.02841601244141,1.10516610493047,1.23124093447851] +
                       [0.317032046082031,0.297732873501953,0.387238668748048,0.417214403517578,0.295067172335937,0.395289340384766,0.299671950496094,0.336251785207031,0.35108569225586,0.397794920205079,0.353934481699219,0.338511888086523,0.377614733638671,0.340975048673829,0.387657576232422,0.298320988382813,0.298564282679688,0.317638243138672,0.291403365121094,0.334383470870703] +
                       [0.107674281397266,0.100976134665039,0.0940538793630859,0.100151858900566,0.0989756802406249,0.0951850062751953,0.0913202687109375,0.095894857875,0.0913387797544921,0.105094817411524,0.108470973105469,0.0933691147460937,0.104291127844922,0.0916368495406251,0.0890392043464843,0.0866653789173827,0.0994091068632812,0.097457315799414,0.0981375326828122,0.092296680451172] +
                       [0.0259585033532031,0.0272081469348047,0.0252789662445313,0.0264197698058789,0.0243723265289063,0.0259858746785156,0.0268263655607422,0.0261431230800781,0.0244658767080078,0.0272478000394531,0.0280767869677344,0.0258036576231445,0.0266777508447266,0.0258713221238281,0.0263499033763672,0.0255020288623047,0.0266601042460937,0.0258135974794922,0.0259851361083985,0.024735744878711] +
                       [0.0124684050390039,0.0124132583474609,0.0119997562419922,0.0119673850147578,0.0116636567716797,0.0118416842732226,0.0119064614949219,0.011658424787461,0.011614185646875,0.012142348390625,0.0110429540431641,0.0121541292595703,0.0119153432408203,0.011003403146875,0.0123993441398437,0.0115732206433594,0.0119643690629102,0.0115232059710938,0.0115091878962891,0.0120726892667969] +
                       [0.0264228154972656,0.0274189557265625,0.0268776604757812,0.0269741724435547,0.0298703968923828,0.0265839626330078,0.0257235049310547,0.026349099255918,0.0264084922601563,0.02660012815625,0.025169687900586,0.0278027306750977,0.0261132362119141,0.0273469215255859,0.0283822489611328,0.0270449024304688,0.0266755212628906,0.0254822723816406,0.0251171353552735,0.0298610275078125] +
                       [0.0988013700332031,0.119488808938965,0.105437458150391,0.0984930047812497,0.103370473067344,0.0934778699972658,0.0979921736919921,0.100527878654297,0.0933729499804687,0.102341221494727,0.0987459765117189,0.100018434628906,0.0982000816523436,0.107628066951563,0.0943635214277342,0.090710258798828,0.0860606746578126,0.100466679150391,0.0934473157771484,0.100048554939453] +
                       [0.294838459048828,0.296339261299414,0.311697490224609,0.309679949160156,0.358731712470703,0.32619758447832,0.366621950978516,0.347158694158203,0.352424206082032,0.32058740336914,0.41721078196289,0.298372869916016,0.411365888121094,0.335983964088868,0.278067457125,0.348074020164063,0.301805085066406,0.397947489958984,0.352582869147657,0.330859994789062] +
                       [1.22869212885957,1.1607267522207,1.07299014137695,1.27449472674805,0.932151729441407,1.03330766838477,1.21756553729492,1.20241047386465,1.12977587459765,1.26932589414063,1.02108398605859,1.1018824945625,0.979793147441406,0.724420707464063,1.23754867263574,1.10327026670898,0.945145244580079,1.16764705344141,1.10706339306055,0.722200776455079]),
  'cherries': np.array([10,15,7,10,9,14,9,11,9,11,13,11,12,10,9,9,10,13,12,11] +
                       [33,36,31,37,34,32,30,33,30,33,31,27,27,37,34,31,30,28,35,28] +
                       [91,88,93,93,93,95,86,87,94,93,96,87,85,102,91,93,88,97,87,100] +
                       [218,234,233,225,227,223,230,224,226,227,226,228,220,235,226,233,223,230,239,231] +
                       [343,354,337,351,342,357,344,335,335,346,339,324,341,337,348,333,335,338,334,338] +
                       [224,219,226,242,225,218,222,225,233,232,229,234,227,233,232,227,223,221,224,228] +
                       [88,85,90,95,86,92,96,88,92,100,81,95,94,91,103,91,92,92,85,95] +
                       [28,34,28,32,31,31,26,30,36,35,26,33,30,30,27,31,26,36,33,38] +
                       [8,8,13,10,11,9,8,11,9,7,11,11,10,10,10,12,7,9,9,9])/1000.
       }
data = pd.DataFrame(data)

# branch lengths
handles = [Patch(color=pal['avg_bl'],label='Average Branch Length'),Patch(color=pal['avg_pen_bl'],label='Average Pendant Branch Length')]
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0,1,2,3,4])
ax = sns.boxplot(x='r',y='avg_bl',data=data,order=x,color=pal['avg_bl'],width=0.3,showfliers=False)
sns.boxplot(x='r',y='avg_pen_bl',data=data,order=x,color=pal['avg_pen_bl'],width=0.3,showfliers=False)
x = np.linspace(-4,4,100)
plt.plot(x+4,avg_bl_vs_r(10**x),linestyle='--',color=pal['avg_bl'])
plt.plot(x+4,avg_pen_bl_vs_r(10**x),linestyle='--',color=pal['avg_pen_bl'])
legend = plt.legend(handles=handles,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., frameon=True)
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}$',fontsize=14)
sns.plt.ylabel('Branch Length',fontsize=14)
sns.plt.title(r'Average Pendant and Overall Branch Length vs. $\log_{10}{r}$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('theoretical_branch-lengths_vs_r.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()

# cherry fraction
fig = plt.figure()
x = np.array([-4,-3,-2,-1,0,1,2,3,4])
ax = sns.boxplot(x='r',y='cherries',data=data,order=x,color=pal['cherries'],width=0.3,showfliers=False)
x = np.linspace(-4,4,100)
plt.plot(x+4,cherries_vs_r(10**x),linestyle='--',color=pal['cherries'])
sns.plt.xlabel(r'$\log_{10}{r} = \log_{10}{\left(\frac{\lambda_A}{\lambda_B}\right)}$',fontsize=14)
sns.plt.ylabel('Cherry Fraction',fontsize=14)
sns.plt.title(r'Cherry Fraction vs. $\log_{10}{r}$',fontsize=18,y=1.05)
sns.plt.show()
fig.savefig('theoretical_cherry-fraction_vs_r.pdf', format='pdf', bbox_extra_artists=(legend,), bbox_inches='tight')
plt.close()