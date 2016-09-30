#! /usr/bin/env python
'''
Niema Moshiri 2016

Perform various basic arithmetic on a list of numbers passed in via STDIN. Only
one number should be on each line of the input. For example, useful to compute
sum/average/etc. of nw_distance output.

Only pass in a single argument.
'''

USAGE_MESSAGE = '''
USAGE: python numlist_math.py [-avg, -sum, -min, -max]
    -avg: Compute average of list of numbers
    -sum: Compute sum of list of numbers
    -min: Compute minimum of list of numbers
    -max: Compute maximum of list of numbers
'''
# imports
import sys

# if code is executed (and not imported)
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("ERROR: Pass in a single argument")
        print(USAGE_MESSAGE)
        exit(-1)
    arg = sys.argv[1].strip().replace('-','')
    l = [float(i) for i in sys.stdin.read().strip().splitlines()]
    if arg == 'avg':
        print(sum(l)/len(l))
    elif arg == 'sum':
        print(sum(l))
    elif arg == 'min':
        print(min(l))
    elif arg == 'max':
        print(max(l))
    else:
        print("ERROR: Invalid argument")
        print(USAGE_MESSAGE)
        exit(-1)