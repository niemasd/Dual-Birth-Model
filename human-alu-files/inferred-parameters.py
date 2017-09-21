#! /usr/bin/env python3
from statistics import stdev
'''
Niema Moshiri 2017

Inferred Alu parameters from subsampling the full dataset
'''

# compute the average of a given list
def avg(x):
    return float(sum(x))/len(x)

# estimate lambda from r and average branch length
def Lambda(r,avg_bl):
    return ((r+1)/(r**0.5))/(2*avg_bl)

# estimate cherry fraction from r
def cherries(r):
    return (r**0.5)/(1+r+(r**0.5))

# compute lambda_A from r and lambda
def lambda_A(r,l):
    return (r*l)/(1+r)

# compute number of right leaves from r
def n_r(r):
    return (r**0.5)/(1+(r**0.5))

# start with just initial r estimates and average (pendant) branch length
data = {
    '1000': {
        'r': [0.00341917197231271,0.00321396780437646,0.00345661241430053,0.00330634577190767,0.00338010070485413,0.00338293870112355,0.00340307198682967,0.00347876282073909,0.00362987630721065,0.00341399342687651,0.00366415356320988,0.00345450810599956,0.00354388962752987,0.00337604386585058,0.00348677513767933,0.00347158112387733,0.00347444038371308,0.00332437822719241,0.0035447757531558,0.00320354475950627],
        'avg_bl': [0.0666031199179177,0.0688266284309306,0.0668386369104103,0.0671783520260259,0.0665746136921921,0.066656165456957,0.0676314796066065,0.06689716291992,0.0675101348428427,0.0670930951396397,0.0661709424169169,0.0671763676806808,0.0680639753703703,0.0669787776351349,0.0679167529734735,0.0662205349509509,0.0670829251226224,0.0684565959804803,0.0665374315920919,0.0662414824159158],
        'avg_pen_bl': [0.119625385146,0.12399297928,0.119983625206,0.12085748825,0.119641986176,0.11978359634,0.12150073628,0.12005054208,0.120891982356,0.12051445414,0.118437303802,0.12059354067,0.122031236116,0.120375424746,0.121866281296,0.118848522588,0.120391354422,0.12312442989,0.119292813742,0.11935443248],
    },
    '10000': {
        'r': [0.00394583622198527,0.00404536682996279,0.00408169853970025,0.00396167904112442,0.00395203652995482,0.00406130983336834,0.00405383209783885,0.00397613189492412,0.00408814229804549,0.00409197729868878,0.00398534039775265,0.00395975039865549,0.00408646240342413,0.00405368937024752,0.00410380805870494,0.00399585271433057,0.00401848574374438,0.0039949052717652,0.00403132102994341,0.00409890263826593],
        'avg_bl': [0.0636422991828176,0.0641711593395836,0.06343470790354,0.0635428817522747,0.0638067860352028,0.0637435256084104,0.0638350263363843,0.0636324734355651,0.0638105598098306,0.0636664450376036,0.064019632029903,0.063143896151765,0.0637837490060497,0.0634952500254018,0.0638995747784273,0.0638364708303334,0.0622574394310929,0.0636676781386631,0.0631016240522552,0.0636323003863386],
        'avg_pen_bl': [0.1134761460965,0.1142688495101,0.1129038180323,0.1132750374124,0.113760053241999,0.113483675864099,0.113657696513,0.1134130185339,0.1135632374957,0.1133010982749,0.1140891537344,0.112566664985,0.1135180070517,0.113052939065499,0.1136984765666,0.1137469419636,0.110900256650401,0.113447598130499,0.1123850510652,0.1132301290327],
    },
    '100000': {
        'r': [0.00409953787343536,0.0041163255609281,0.00392242251485858,0.00403924447941364,0.00395856555161129,0.00403539225880063,0.00407890664975576,0.00412798863093909,0.00401189491065905,0.00394376002980995,0.00398104300291373,0.00398704644476533,0.00407113624989654,0.00388605621659614,0.00402397367283451,0.00416667680040088,0.00397787229696555,0.00400411290903793,0.00399414142929841,0.00398118286613707],
        'avg_bl': [0.0636246324955002,0.0630730860513074,0.0640252057993298,0.0624844993467846,0.0633256100457543,0.0639255099096411,0.0629667784398943,0.0629214638904895,0.0626088326779178,0.0641237727338237,0.0638920083864383,0.0630591519255929,0.0637475201951194,0.0636349431930694,0.0635715722376741,0.0626235100729071,0.0637596082947794,0.063642942342434,0.0637305088889394,0.0628767294029398],
        'avg_pen_bl': [0.1132155490246,0.1122096376708,0.1141944997341,0.1112743669788,0.1128923820816,0.1138463193046,0.112075057875,0.1119229713906,0.1115358774841,0.114337785943,0.1138681887317,0.1123749507399,0.1134762142655,0.1135536881774,0.1132329697087,0.1113373227463,0.1136369941952,0.113389743926399,0.1135606999216,0.112058553508701],
    },
    '885011FT': {
        'r': [0.005974453968672819],
        'avg_bl': [0.0550398731181634],
        'avg_pen_bl': [0.0958369619839419],
    },
    '885011RAxML': {
        'r': [0.006302343376798612],
        'avg_bl': [0.0545912750125638],
        'avg_pen_bl': [0.0947376819067773]
    }
}

# estimate lambda
for n in data:
    data[n]['lambda'] = [Lambda(data[n]['r'][i],data[n]['avg_bl'][i]) for i in range(len(data[n]['r']))]

# compute lambda_A and lambda_b
for n in data:
    data[n]['lambda_a'] =[lambda_A(data[n]['r'][i],data[n]['lambda'][i]) for i in range(len(data[n]['r']))]
    data[n]['lambda_b'] = [(data[n]['lambda'][i]-data[n]['lambda_a'][i]) for i in range(len(data[n]['r']))]

# compute number of right leaves
for n in data:
    data[n]['n_r'] = [n_r(data[n]['r'][i]) for i in range(len(data[n]['r']))]

# output data cleanly
COLS = ['n_r','r','lambda','lambda_a','lambda_b','avg_bl','avg_pen_bl']
pad = {'n_r':'            ','r':'              ','lambda':'           ','lambda_a':'       ','lambda_b':'         ','avg_bl':'         ','avg_pen_bl':'     '}
head = '| n           | ' + ' | '.join([e + pad[e] for e in COLS]) + ' |'
print(head)
print('-'*len(head))
for n in sorted(data.keys()):
    print('| ' + str(n),end=(11-len(str(n)))*' ' + ' | ')
    for col in COLS:
        print("%0.4f" % avg(data[n][col]),end=' ± ')
        try:
            s = stdev(data[n][col])
        except:
            s = 0
        print("%0.4f" % s,end=' | ')
    print()