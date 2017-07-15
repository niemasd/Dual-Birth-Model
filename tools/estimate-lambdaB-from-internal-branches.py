#!/usr/bin/env python3
import argparse
from sys import stdin,stderr
from math import exp,log
from numpy import percentile
from detect_peaks import detect_peaks
from datetime import datetime
VERBOSE = False
TOL = 0.000001

# compute average of list x
def avg(x):
    return sum(x)/float(len(x))

# niema's peak-calling approach to estimating lambdaB
def peak_calling(x,mode):
    valley = {'v':True,'p':False}[mode[1]]
    lbs = [(-1*log(1-p/100.))/percentile(x,p) for p in range(1,100)]
    indices = detect_peaks(lbs,valley=valley)
    critlbs = [lbs[i] for i in indices]
    lb = {'m':min,'M':max,'a':avg}[mode[0]](critlbs)
    return lb

# v_i^t function for the EM algorithm for a single number x_i
def vi(xi,a,b,k):
    return (a*exp(-1*a*xi)*k) / ((a*exp(-1*a*xi)*k) + b*exp(-1*b*xi)*(1-k))

# EM approach to estimating lambdaB (https://stats.stackexchange.com/questions/291642/how-to-estimate-parameters-of-mixture-of-2-exponential-random-variables-ideally)
def em(x,tol):
    # initialize
    n = len(x)
    xAvg = avg(x)
    a = 1.0/xAvg
    b = 1.0/xAvg
    k = 0.5

    # EM algorithm
    num_it = 0
    while True:
        # store old values
        num_it += 1
        aOld = a
        bOld = b
        kOld = k

        # E step
        v = [vi(xi,a,b,k) for xi in x]
        # M step
        sumV = float(sum(v))
        k = sumV/float(n)
        lambda1 = sumV/sum([v[i]*x[i] for i in range(n)])
        lambda2 = n - sumV
        a = min(lambda1,lambda2)
        b = max(lambda1,lambda2)

        # check for termination
        if abs(a-aOld) + abs(b-bOld) + abs(k-kOld) < tol:
            break

    # return converged parameters
    if VERBOSE:
        stderr.write('[%s] Number of EM Iterations: %d\n' % (datetime.now(),num_it))
    return a,b,k

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-m', '--mode', required=False, type=str, default='mp', help="Mode (mv = min valley, Mv = Max valley, av = average valley, mp = min peak, Mp = Max peak, ap = average peak, em = EM method, mpem = min peak averaged with EM method, mvem = min valley averaged with EM method)")
    parser.add_argument('-t', '--tol', required=False, type=float, default=TOL, help="Tolerance in EM (unused in other modes)")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable Verbose Messages")
    args = parser.parse_args()
    VERBOSE = args.verbose
    assert args.mode in {'mv','Mv','av','mp','Mp','ap','em','mpem','mvem'}, "Mode must be in {mv,Mv,av,mp,Mp,ap,em,mpem,mvem}. Use -h for help"
    x = [float(x) for x in stdin.read().split()]
    if args.mode in {'mv','Mv','av','mp','Mp','ap'}:
        lb = peak_calling(x,args.mode)
    elif args.mode == 'em':
        la,lb,k = em(x,args.tol)
        #print("lambdaA = %f, lambdaB = %f, k = %f" % (la,lb,k))
    elif args.mode in {'mpem','mvem'}:
        lb_peak = peak_calling(x,args.mode[:2])
        la_em,lb_em,k_em = em(x,args.tol)
        lb = (lb_peak+lb_em)/2
    print(lb)