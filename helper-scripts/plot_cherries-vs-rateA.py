'''
Niema Moshiri 2016
Generate plots of number of cherries vs. rateA (activation rate)
'''
# imports
import re                            # for regex search to count cherries
import matplotlib.pyplot as plt      # for plotting
import seaborn                       # for plotting (prettier)
from math import sqrt                # for calculation of stdev
from math import log                 # for calculation of log ratios
from scipy.optimize import curve_fit # for curve fitting
from numpy import asarray            # for curve fitting
from multiprocessing import Pool     # for multiprocessig
import sys                           # to import simulateAlu
sys.path.insert(0,'../tools')        # to import simulateAlu
from AluSimulator import simulateAlu # for Alu tree simulation

# define some things for convenience
cherryRegex = '\([0-9]+\:[0-9]+\.?[0-9]+e?-?[0-9]*\,[0-9]+\:[0-9]+\.?[0-9]+e?-?[0-9]*\)'
rateB = 10000 # choose large (B)irth Rate
n     = 1000  # trees will have 1000 leaves
reps  = 100   # for each rateA, simulate this many trees (repetitions)

# set up rateAs
rateAs = [1,5,10,20,50,100,200,500,1000,2000,5000,10000] # (A)ctivation Rates
for r in rateAs[:-1]:
    rateAs.append(int(rateB*rateB/r))
rateAs = sorted(rateAs)
cherries = []
errors = []

# helper function for tree simulations in multithreading
def callSimulator(args):
    return simulateAlu(args[0], args[1], args[2])

# perform simulations
for rateA in rateAs:
    # simulate trees
    pool = Pool(processes=reps)
    trees = pool.map(callSimulator, [(rateA, rateB, n) for _ in range(reps)])
    pool.close()
    pool.join()

    # compute stats
    sumCherries = 0.0
    sqSumCherries = 0.0
    for tree in trees:
        numCherries = len(re.findall(cherryRegex,tree))
        sumCherries += numCherries
        sqSumCherries += (numCherries*numCherries)
    mean = sumCherries/reps
    stdev = sqrt((sqSumCherries/reps) - (mean*mean))
    cherries.append(mean)
    errors.append(stdev)

# fit curve (y = alpha - beta/x)
'''
def func(x, alpha, beta):
    return alpha - (beta/x)
popt, pcov = curve_fit(func, asarray(rateAs), asarray(cherries))
print("NumCherries = " + str(popt[0]) + " - " + str(popt[1]) + "/(Activation Rate)\n")
'''

# create plot of Number of Cherries vs. Log2 of Activation Rate (rateA)
logs = [log(rateA) for rateA in rateAs]
plt.figure()
plt.errorbar(logs, cherries, yerr=errors)
plt.title("Number of Cherries vs. Log2 of Activation Rate (rateA) for Birth Rate (rateB) = " + str(rateB))
plt.ylabel("Number of Cherries")
plt.xlabel("Log2 of Activation Rate (rateA)")
plt.show()

# create plot of Number of Cherries vs. Log2-Ratio of Rates (rateB/rateA)
ratios = [log(float(rateB)/float(rateA), 2) for rateA in rateAs] # log-2 ratios
plt.clf()
plt.errorbar(ratios, cherries, yerr=errors)
plt.title(r"Number of Cherries vs. Log-Ratio of Rates $(\frac{rateB}{rateA})$ for Birth Rate (rateB) = " + str(rateB))
plt.ylabel("Number of Cherries")
plt.xlabel(r"Log2-Ratio of Rates $(\frac{rateB}{rateA})$")
plt.show()