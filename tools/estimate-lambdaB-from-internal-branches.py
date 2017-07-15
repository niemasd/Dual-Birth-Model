#!/usr/bin/env python3
import argparse
from sys import stdin
from math import log
from numpy import percentile
from detect_peaks import detect_peaks

def avg(x):
    return sum(x)/float(len(x))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-m', '--mode', required=False, type=str, default='mp', help="Mode (mv = min valley, Mv = Max valley, av = average valley, mp = min peak, Mp = Max peak, ap = average peak)")
    args = parser.parse_args()
    assert args.mode in {'mv','Mv','av','mp','Mp','ap'}, "Mode must be {mv,Mv,mp,Mp}. Use -h for help"
    valley = {'v':True,'p':False}[args.mode[1]]
    x = [float(x) for x in stdin.read().split()]
    lbs = [(-1*log(1-p/100.))/percentile(x,p) for p in range(1,100)]
    indices = detect_peaks(lbs,valley=valley)
    critlbs = [lbs[i] for i in indices]
    lb = {'m':min,'M':max,'a':avg}[args.mode[0]](critlbs)
    print(lb)
