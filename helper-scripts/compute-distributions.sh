#!/bin/bash

python tools/AluSimulator.py 1 1 6 50000|nw_topology -IL -|nw_order -ca - |sort|uniq -c|sort -k2n|tee ur.txt

python tools/AluSimulator.py 1 1 6 50000|nw_topology -L -|nw_order -ca - |sort|uniq -c|sort -k2n|tee r.txt
