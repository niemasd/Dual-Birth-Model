#!/usr/bin/env python3
'''
Estimate r given a Newick tree using average branch length and average terminal
branch length.
'''
from sys import stdin
from os.path import expanduser,isfile
from subprocess import Popen,PIPE,STDOUT
import argparse

# possible correction methods
def none(bl,pen_bl):
    return bl,pen_bl
METHODS = {None:none}

# generally useful functions
def sqrt(x):
    return x**0.5
def avg(x):
    return sum(x)/float(len(x))

# estimate r from average branch length (b) and average terminal branch length (l)
def r(bl,pen_bl):
    b = avg(bl)
    l = avg(pen_bl)
    if b > l:
        return 1
    return (-2*(b**3) + 5*(b**2)*l - 3*b*(l**2) + 2*sqrt(2)*sqrt(-1*(b**2)*((b-l)**3)*l)) / (b*(b-l)*l)

# main function
if __name__ == "__main__":
    # parse user args
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-t', '--treefile', required=False, type=str, default='stdin', help="Tree File (Newick format)")
    parser.add_argument('-c', '--correction', required=False, type=str, default=None, help="Correction Method %s" % str(sorted(METHODS.keys())))
    args = parser.parse_args()
    assert args.correction in METHODS, "Incorrect correction method. Use -h to see options"

    # read tree parameters
    if args.treefile == 'stdin': # read from stdin
        tree = stdin.read().strip().encode('utf-8')
        bl = [float(i) for i in Popen(['nw_distance','-mp','-sa','-'], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate(input=tree)[0].decode().split()]
        pen_bl = [float(i) for i in Popen(['nw_distance','-mp','-sf','-'], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate(input=tree)[0].decode().split()]
    else:
        args.treefile = expanduser(args.treefile)
        assert isfile(args.treefile), "No such file: %s" % args.treefile
        bl = [float(i) for i in check_output(['nw_distance','-mp','-sa',args.treefile]).split()]
        pen_bl = [float(i) for i in check_output(['nw_distance','-mp','-sf',args.treefile]).split()]

    # estimate r (potentially after correcting branch lengths)
    fixed_bl,fixed_pen_bl = METHODS[args.correction](bl,pen_bl)
    print(r(fixed_bl,fixed_pen_bl))