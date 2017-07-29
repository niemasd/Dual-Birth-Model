#!/usr/bin/env python3
'''
Estimate r given a Newick tree using average branch length and average terminal
branch length.
'''
from sys import stdin
from os.path import expanduser,isfile
from subprocess import Popen,PIPE,STDOUT
import argparse
def sqrt(x):
    return x**0.5

# estimate r from average branch length (b) and average terminal branch length (l)
def r(b,l):
    if b > l:
        return 1
    return (-2*(b**3) + 5*(b**2)*l - 3*b*(l**2) + 2*sqrt(2)*sqrt(-1*(b**2)*((b-l)**3)*l)) / (b*(b-l)*l)

# main function
if __name__ == "__main__":
    # parse user args
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t', '--treefile', required=False, type=str, default='stdin', help="Tree File (Newick format)")
    args = parser.parse_args()

    # read tree parameters
    if args.treefile == 'stdin': # read from stdin
        tree = stdin.read().strip().encode('utf-8')
        BL = sorted([float(i) for i in Popen(['nw_distance','-mp','-sa','-'], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate(input=tree)[0].decode().split()])
        PEN_BL = sorted([float(i) for i in Popen(['nw_distance','-mp','-sf','-'], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate(input=tree)[0].decode().split()])
    else:
        args.treefile = expanduser(args.treefile)
        assert isfile(args.treefile), "No such file: %s" % args.treefile
        BL = sorted([float(i) for i in check_output(['nw_distance','-mp','-sa',args.treefile]).split()])
        PEN_BL = sorted([float(i) for i in check_output(['nw_distance','-mp','-sf',args.treefile]).split()])
    AVG_BL = sum(BL)/len(BL)
    AVG_PEN_BL = sum(PEN_BL)/len(PEN_BL)

    # estimate r using avg. branch length and avg. terminal branch length
    print(r(AVG_BL,AVG_PEN_BL))