#! /usr/bin/env python3
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

# start with just initial r estimates and average branch length
data = {
    1000: {
        'r': [0.00198841560450622,0.00201484714526581,0.00187470156084909,0.00197184792151436,0.00182477568343849,0.00202334943610643,0.00208909760593108,0.00196029317604756,0.00205766559195526,0.00205779682736656,0.00209471769366492,0.00206352512937753,0.00202825673281893,0.00202378138351705,0.00208235921287866,0.00205296142918066,0.001937729970609,0.00198049826484789,0.00203891083430367,0.00201156486353665],
        'avg_bl': [0.0783930319307305,0.0805310268718718,0.0787191591115315,0.0792799472742741,0.077441059319039,0.0766205847357356,0.111668308473473,0.0801464374211711,0.075458044551051,0.0792936809878477,0.0799468541673172,0.0781147958563563,0.0789104714679677,0.0792843361976976,0.0810571153203204,0.0797717191740741,0.106441352164064,0.122600752498999,0.0800363982157155,0.0766766655460459]
    },
    885011: {
        'r': [0.005974453968672819],
        'avg_bl': [0.0550398731181634]
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
for n in sorted(data.keys()):
    print(n,end='\t')
    for col in ['n_r','r','lambda','lambda_a','lambda_b','avg_bl']:
        print(avg(data[n][col]),end='\t')
    print()