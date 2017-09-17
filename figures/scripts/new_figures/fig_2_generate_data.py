#! /usr/bin/env python3
import numpy as np
from subprocess import check_output
N = 4096
LAMBDA = 48
MIN_LOG_R = -4
MAX_LOG_R = 4
NUM_POINTS = 32+1 # +1 for log(r) = 0
NUM_REPS = 100
STEP = (MAX_LOG_R-MIN_LOG_R)/(NUM_POINTS-1)

# generate data
data = {'r':[],'avg_bl':[],'avg_pen_bl':[],'cherries':[]}
for logr in np.arange(MIN_LOG_R,MAX_LOG_R+STEP,STEP):
    r = 10**logr
    la = (LAMBDA*r)/(r+1)
    lb = LAMBDA-la
    for rep in range(NUM_REPS):
        #tree = check_output(['../../../tools/DualBirthSimulator.py','-la',str(la),'-lb',str(lb),'-n',str(N)]).decode().strip()
        tree = check_output(['/Users/niema/GitHub/Dual-Birth-Simulator/dualbirth',str(la),str(lb),'-n',str(N)]).decode().strip()
        avg_bl = float(check_output('echo "%s" | nw_distance -mp -sa - | numlist -avg' % tree,shell=True))
        avg_pen_bl = float(check_output('echo "%s" | nw_distance -mp -sf - | numlist -avg' % tree,shell=True))
        cherries = float(check_output('echo "%s" | ../../../helper-scripts/count_cherries.sh' % tree,shell=True))
        data['r'].append(logr)
        data['avg_bl'].append(avg_bl)
        data['avg_pen_bl'].append(avg_pen_bl)
        data['cherries'].append(cherries/N)
f = open('fig_2_data.json','w')
f.write(str(data))
f.close()