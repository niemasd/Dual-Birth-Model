#! /usr/bin/env python3
import numpy as np
from subprocess import check_output
N = 4096
LAMBDA = 48
MIN_LOG_R = -4
MAX_LOG_R = 0
NUM_POINTS = 16+1 # +1 for log(r) = 0
NUM_REPS = 100
STEP = (MAX_LOG_R-MIN_LOG_R)/(NUM_POINTS-1)

# generate data
data = {'r':[],'var_bl':[],'var_pen_bl':[]}
for logr in np.arange(MIN_LOG_R,MAX_LOG_R+STEP,STEP):
    r = 10**logr
    la = (LAMBDA*r)/(r+1)
    lb = LAMBDA-la
    for rep in range(NUM_REPS):
        tree = check_output(['/Users/niema/GitHub/Dual-Birth-Simulator/dualbirth',str(la),str(lb),'-n',str(N)]).decode().strip()
        var_bl = float(check_output('echo "%s" | nw_distance -mp -sa - | numlist -var' % tree,shell=True))
        var_pen_bl = float(check_output('echo "%s" | nw_distance -mp -sf - | numlist -var' % tree,shell=True))
        data['r'].append(logr)
        data['var_bl'].append(var_bl)
        data['var_pen_bl'].append(var_pen_bl)
f = open('fig_s2_data.json','w')
f.write(str(data))
f.close()