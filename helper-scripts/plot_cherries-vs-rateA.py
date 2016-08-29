'''
Niema Moshiri 2016
Generate plots of number of cherries vs. rateA (activation rate)
'''
# imports
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from math import sqrt
import sys
sys.path.insert(0,'../tools')
from AluSimulator import simulateAlu

# define some things for convenience
cherryRegex = '\([0-9]+\:[0-9]+\.?[0-9]+e?-?[0-9]*\,[0-9]+\:[0-9]+\.?[0-9]+e?-?[0-9]*\)'
rateB = 10000 # choose large (B)irth Rate
n     = 1000  # trees will have 1000 leaves
reps  = 100   # for each rateA, simulate this many trees (repetitions)

# perform simulations
rateAs = [1,5,10,20,50,100,200,500,1000,2000,5000,10000] # (A)ctivation Rates
cherries = []
errors = []
for rateA in rateAs:
    sumCherries = 0.0
    sqSumCherries = 0.0
    for it in xrange(reps):
        tree = simulateAlu(rateA,rateB,n)
        numCherries = len(re.findall(cherryRegex,tree))
        sumCherries += numCherries
        sqSumCherries += (numCherries*numCherries)
    mean = sumCherries/reps
    stdev = sqrt((sqSumCherries/reps) - (mean*mean))
    cherries.append(mean)
    errors.append(stdev)

# create plot
plt.figure()
plt.errorbar(rateAs, cherries, yerr=errors)
plt.title("Number of Cherries vs. Activation Rate (rateA)")
plt.ylabel("Number of Cherries")
plt.xlabel("Activation Rate (rateA)")
plt.show()