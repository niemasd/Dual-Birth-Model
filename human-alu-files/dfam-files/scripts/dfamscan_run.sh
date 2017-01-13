file="${1##*/}"
/home/nmoshiri/bin/hmmer-3.1b2-linux-intel-x86_64/binaries/dfamscan.pl -fastafile $1 -hmmfile /home/nmoshiri/siavash_research/Dfam/Dfam.humanAlu.hmm -dfam_outfile $file.alu
