#!/usr/bin/env python3
'''
Estimate r given a Newick tree using average branch length and average terminal
branch length.
'''
from sys import argv,stdin
from math import exp,log
from os.path import expanduser,isfile
from subprocess import Popen,PIPE,STDOUT
import argparse
from numpy import percentile

# possible correction methods
def none(bl,pen_bl): # no correction
    return bl,pen_bl
def bootlier(bl,pen_bl): # remove outliers using distribution-free method in Candelon & Metiu 2013 (https://github.com/jodeleeuw/Bootlier)
    bootlier_path = '/'.join(argv[0].split('/')[:-2] + ['deps','bootlier.R'])
    bl_script = "source('%s')\ndata <- c(%s)\nresult <- bootstrap.identify.outliers(data)\nprint(result$data.truncated)" % (bootlier_path, str(bl)[1:-1])
    out = Popen(['R','--slave'], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate(input=bl_script.encode('utf-8'))[0].decode()
    bl_fixed = [float(i) for line in out.splitlines()[3:] for i in line.split()[1:]]
    pen_bl_script = "source('%s')\ndata <- c(%s)\nresult <- bootstrap.identify.outliers(data)\nprint(result$data.truncated)" % (bootlier_path, str(pen_bl)[1:-1])
    out = Popen(['R','--slave'], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate(input=pen_bl_script.encode('utf-8'))[0].decode()
    pen_bl_fixed = [float(i) for line in out.splitlines()[3:] for i in line.split()[1:]]
    return bl_fixed,pen_bl_fixed
def bootlier_log(bl,pen_bl): # remove outliers using Bootlier on log-scaled lengths
    log_bl_fixed,log_pen_bl_fixed = bootlier([log(i) for i in bl if i > 0],[log(i) for i in pen_bl if i > 0])
    return [exp(i) for i in log_bl_fixed],[exp(i) for i in log_pen_bl_fixed]
def bootlier_log_above_med(bl,pen_bl): # remove outliers above median using Bootlier on log-scaled lengths
    med_bl = percentile(bl,50)
    med_pen_bl = percentile(pen_bl,50)
    bl_filtered,pen_bl_filtered = bootlier_log(bl,pen_bl)
    bl_filtered_set = set(bl_filtered)
    pen_bl_filtered_set = set(pen_bl_filtered)
    for l in bl:
        if l < med_bl and l not in bl_filtered_set:
            bl_filtered.append(l)
    for l in pen_bl:
        if l < med_pen_bl and l not in pen_bl_filtered_set:
            pen_bl_filtered.append(l)
    return sorted(bl_filtered),sorted(pen_bl_filtered)
def bootlier_log_below_med(bl,pen_bl): # remove outliers below median using Bootlier on log-scaled lengths
    med_bl = percentile(bl,50)
    med_pen_bl = percentile(pen_bl,50)
    bl_filtered,pen_bl_filtered = bootlier_log(bl,pen_bl)
    bl_filtered_set = set(bl_filtered)
    pen_bl_filtered_set = set(pen_bl_filtered)
    for l in bl:
        if l > med_bl and l not in bl_filtered_set:
            bl_filtered.append(l)
    for l in pen_bl:
        if l > med_pen_bl and l not in pen_bl_filtered_set:
            pen_bl_filtered.append(l)
    return sorted(bl_filtered),sorted(pen_bl_filtered)
def bootlier_log_above_p75(bl,pen_bl): # remove outliers above 75th percentile using Bootlier on log-scaled lengths
    p75_bl = percentile(bl,75)
    p75_pen_bl = percentile(pen_bl,75)
    bl_filtered,pen_bl_filtered = bootlier_log(bl,pen_bl)
    bl_filtered_set = set(bl_filtered)
    pen_bl_filtered_set = set(pen_bl_filtered)
    for l in bl:
        if l < p75_bl and l not in bl_filtered_set:
            bl_filtered.append(l)
    for l in pen_bl:
        if l < p75_pen_bl and l not in pen_bl_filtered_set:
            pen_bl_filtered.append(l)
    return sorted(bl_filtered),sorted(pen_bl_filtered)
def bootlier_log_below_p25(bl,pen_bl): # remove outliers above 25th percentile using Bootlier on log-scaled lengths
    p25_bl = percentile(bl,25)
    p25_pen_bl = percentile(pen_bl,25)
    bl_filtered,pen_bl_filtered = bootlier_log(bl,pen_bl)
    bl_filtered_set = set(bl_filtered)
    pen_bl_filtered_set = set(pen_bl_filtered)
    for l in bl:
        if l > p25_bl and l not in bl_filtered_set:
            bl_filtered.append(l)
    for l in pen_bl:
        if l > p25_pen_bl and l not in pen_bl_filtered_set:
            pen_bl_filtered.append(l)
    return sorted(bl_filtered),sorted(pen_bl_filtered)
METHODS = {None:none,'bootlier':bootlier,'bootlier_log':bootlier_log,'bootlier_log_above_med':bootlier_log_above_med,'bootlier_log_below_med':bootlier_log_below_med,'bootlier_log_above_p75':bootlier_log_above_p75,'bootlier_log_below_p25':bootlier_log_below_p25}

# generally useful functions
def sqrt(x):
    return x**0.5
def avg(x):
    return sum(x)/float(len(x))

# estimate r from average branch length (b) and average terminal branch length (l)
def r(bl,pen_bl):
    if len(bl) == 0 or len(pen_bl) == 0:
        return 1
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
    parser.add_argument('-c', '--correction', required=False, type=str, default=None, help="Correction Method %s" % ("(Options: " + str(sorted([str(key) for key in METHODS]))[1:-1] + ")"))
    args = parser.parse_args()
    if args.correction is not None:
        args.correction = args.correction.lower()
    assert args.correction in METHODS, "Incorrect correction method. Use -h to see options"

    # read tree parameters
    if args.treefile == 'stdin': # read from stdin
        tree = stdin.read().strip().encode('utf-8')
        bl = [float(i) for i in Popen(['nw_distance','-mp','-sa','-'], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate(input=tree)[0].decode().split() if str(float(i)) != 'nan']
        pen_bl = [float(i) for i in Popen(['nw_distance','-mp','-sf','-'], stdout=PIPE, stdin=PIPE, stderr=STDOUT).communicate(input=tree)[0].decode().split() if str(float(i)) != 'nan']
    else:
        args.treefile = expanduser(args.treefile)
        assert isfile(args.treefile), "No such file: %s" % args.treefile
        bl = [float(i) for i in check_output(['nw_distance','-mp','-sa',args.treefile]).split() if str(float(i)) != 'nan']
        pen_bl = [float(i) for i in check_output(['nw_distance','-mp','-sf',args.treefile]).split() if str(float(i)) != 'nan']

    # estimate r (potentially after correcting branch lengths)
    fixed_bl,fixed_pen_bl = METHODS[args.correction](bl,pen_bl)
    print(r(fixed_bl,fixed_pen_bl))