# USAGE: DfamScanToFASTA.py <dfamscan_output> <ref_genome>

# reverse complement of a DNA string
def revC(s):
    return ''.join([{'A':'T','T':'A','C':'G','G':'C','N':'N'}[c] for c in s])[::-1]

import sys
from Bio import SeqIO
if len(sys.argv) != 3:
    print "ERROR: Incorrect number of arguments"
    print "USAGE: DfamScanToFASTA.py <dfamscan_output> <ref_genome>"
    exit(-1)

# get organism name
organism = sys.argv[2].split('/')[-1].split('_')[0]

# read in reference genome
genome = {}
for chr in SeqIO.parse(open(sys.argv[2]),'fasta'):
    genome[chr.id] = str(chr.seq)

# convert DfamScan output to FASTA
for line in open(sys.argv[1]):
    # ignore header lines
    if line[0] != '#':
        # split line correctly (dfamscan uses multi-spaces instead of tabs)
        parts = line.strip().split()
        desc = ' '.join(parts[14:])
        parts = parts[:14] + [desc]

        # extract relevant sequence stuff
        chrom = parts[2]
        strand = parts[8]
        aliStart = int(parts[9])
        aliEnd = int(parts[10])

        # print this entry as FASTA
        print '>' + organism + ' | ' + ' | '.join(parts)
        if strand == '+':
            print genome[chrom][aliStart:aliEnd+1].upper()
        else:
            print revC(genome[chrom][aliEnd:aliStart+1].upper())
