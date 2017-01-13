# USAGE: python ExtractHumanAluDfam.py <Dfam.hmm_file>
import sys
if len(sys.argv) != 2:
    print "ERROR: Incorrect number of arguments"
    print "USAGE: python ExtractHumanAluDfam.py <Dfam.hmm_file>"
    exit(-1)

# read in Dfam header
f = open(sys.argv[1]).read().splitlines()
header = []
for line in f:
    if line[0] == '#':
        header.append(line)
    else:
        break
f = ('\n'.join(f[len(header):])).split('\n//\n')
header = '\n'.join(header)

# filter sequences that are human and Alu
out = []
for entry in f:
    if "SubType: Alu" in entry and "TaxName:Homo sapiens;" in entry:
        out.append(entry)
print header
print '\n//\n'.join(out)
