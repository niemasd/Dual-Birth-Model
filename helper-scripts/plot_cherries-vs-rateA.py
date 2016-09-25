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
from math import exp                 # for fitting to Gaussian function
from scipy.optimize import curve_fit # for curve fitting
from scipy import asarray as ar,exp  # for curve fitting
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

# create plot of Number of Cherries vs. Log2 of Activation Rate (rateA)
logs = [log(rateA) for rateA in rateAs]
plt.figure()
plt.errorbar(logs, cherries, yerr=errors)
plt.title("Number of Cherries vs. Log2 of Activation Rate (rateA) for Birth Rate (rateB) = " + str(rateB))
plt.ylabel("Number of Cherries")
plt.xlabel("Log2 of Activation Rate (rateA)")
plt.show()

# compute ratios
ratios = [log(float(rateB)/float(rateA), 2) for rateA in rateAs] # log-2 ratios

# regular Gaussian function (https://en.wikipedia.org/wiki/Gaussian_function)
def gaussian(x, a, b, c):
    return a*exp(-1*(((x-b)**2)/(2*(c**2))))

# Gaussian function forced to be centered at x = 0
def gaussianCentered(x, a, c):
    return a*exp(-1*((x**2)/(2*(c**2))))

# Gaussian function with 1 added (because # cherries is at least 1)
def gaussianPlusOne(x, a, b, c):
    return a*exp(-1*(((x-b)**2)/(2*(c**2)))) + 1

# Gaussian function forced to be centered at x = 0 with the 1 added
def gaussianCenteredPlusOne(x, a, c):
    return a*exp(-1*((x**2)/(2*(c**2)))) + 1

myFunc = gaussianCenteredPlusOne # change this to the function you want to fit
print("Let x be the Log2-Ratio of rateB and rateA (i.e., x = log(rateB/rateA))")
print("Fitting to Gaussian function...")
if myFunc == gaussianCentered or myFunc == gaussianCenteredPlusOne:
    print("Forcing the curve to be centered at x = 0")
popt, pcov = curve_fit(myFunc, ar(ratios), ar(cherries))
print("a = " + str(popt[0]))
if myFunc == gaussian or myFunc == gaussianPlusOne:
    print("b = " + str(popt[1]))
    print("c = " + str(popt[2]))
else:
    print("b = 0")
    print("c = " + str(popt[1]))

# create plot of Number of Cherries vs. Log2-Ratio of Rates (rateB/rateA)
plt.clf()
plt.errorbar(ratios, cherries, yerr=errors, color='blue', label="data")
plt.errorbar(ratios, myFunc(ar(ratios), *popt), color='red', label="fit")
plt.title(r"Number of Cherries vs. Log-Ratio of Rates $(\log_2{(\frac{rateB}{rateA})})$ for Birth Rate (rateB) = " + str(rateB))
plt.ylabel("Number of Cherries")
plt.xlabel(r"Log2-Ratio of Rates $(\log_2{(\frac{rateB}{rateA})})$")
plt.legend()
plt.show()