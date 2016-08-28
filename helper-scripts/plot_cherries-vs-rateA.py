'''
Niema Moshiri 2016
Generate plots of number of cherries vs. rateA (activation rate)
'''
# imports
import sys
sys.path.insert(0,'../tools')
from AluSimulator import simulateAlu

# perform simulations
rateB = 10000 # choose large (B)irth Rate
n     = 1000  # trees will have 1000 leaves
#for rateA in [1,5,10,50,100,500,1000,5000,10000]: # (A)ctivation Rates
for rateA in [100]:
    tree = simulateAlu(rateA,rateB,n)
    print(tree)