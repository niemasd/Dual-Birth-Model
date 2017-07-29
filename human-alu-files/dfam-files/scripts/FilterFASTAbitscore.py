# USAGE: python FilterFASTAbitscore.py <input_dfam_fasta> <bitscore_threshold_json>
import sys
if len(sys.argv) != 3:
    print "ERROR: Incorrect number of arguments"
    print "USAGE: python FilterFASTAbitscore.py <input_dfam_fasta> <bitscore_threshold_json>"
    exit(-1)
thresh = eval(''.join(open(sys.argv[2]).read().strip()))
f = open(sys.argv[1]).read().splitlines()
for i in xrange(0,len(f),2):
    parts = f[i].split(' | ')
    alu,bitscore = parts[1],float(parts[4])
    if float(bitscore) >= thresh[alu]:
        print f[i].strip()
        print f[i+1].strip()
