#! /usr/bin/env python
'''
Niema Moshiri 2016

Generate an INDELible control file to generate sequences for a set of trees
using the GTR model.
'''

USAGE_MESSAGE = '''
USAGE:   python generate-indelible-control.py <directory> <length> <replicates> <gtr_freqs> <gtr_rates> <alpha>
    -directory:  Directory containing trees (in Newick format), either .tre or .tre.gz
    -length:     Length of root sequence
    -replicates: Number of replicate datasets to generate
    -gtr_freqs:  GTR State Frequencies in the format pA,pC,pG,pT (comma-delimited, no spaces)
    -gtr_rates:  GTR Substitution Rates in the format pAC,pAG,pAT,pCG,pCT,pGT (comma-delimited, no spaces)
    -alpha:      Shape parameter for the gamma distribution for sequence evolution

EXAMPLE: python generate-indelible-control.py ~/myTrees 300 1 0.2922,0.2319,0.2401,0.2358 0.8896,2.9860,0.8858,1.0657,3.8775,1.0000 5.256
'''
# imports
import gzip,os,re,sys

# convert scientific notation string to float (INDELible can't parse scientific notation)
def sci_to_float(match):
    return format(float(match.group()), '.12f')

# generate control file and output as string (which can be written to file)
def generateControl(directory, length, reps, pA, pC, pG, pT, pAC, pAG, pAT, pCG, pCT, pGT, alpha):
    # normalize substitution rates so pAG = 1 for INDELible (as opposed to pGT = 1 for FastTree)
    pAC /= pAG
    pAT /= pAG
    pCG /= pAG
    pCT /= pAG
    pGT /= pAG
    pAG = 1.0

    # add GTR parameters
    control = (
"/* GTR State Frequencies:  pA = " + str(pA) + ", pC = " + str(pC) + ", pG = " + str(pG) + ", pT = " + str(pT) + " */\n" +
"/* GTR Substitution Rates: pAC = " + str(pAC) + ", pAG = " + str(pAG) + ", pAT = " + str(pAT) + ", pCG = " + str(pCG) + ", pCT = " + str(pCT) + ", pGT = " + str(pGT) + ' */\n'
"/* Gamma Distribution:     alpha = " + str(alpha) + ''' */

/* Nucleotide Simulation */
[TYPE] NUCLEOTIDE 1 // use Method 1 (usually faster)

/* GTR Model */
[MODEL] GTRalu  // model name
    [submodel]  GTR ''' + str(pCT) + ' ' + str(pAT) + ' ' + str(pGT) + ' ' + str(pAC) + ' ' + str(pCG) + '''
    [statefreq] ''' + str(pT) + ' ' + str(pC) + ' ' + str(pA) + ' ' + str(pG)) + '''
    [rates]     0 ''' + str(alpha) + ' 0\n\n'

    # add trees
    control += "/* Trees (Newick format) */\n"
    trees = []
    for f in os.listdir(directory):
        tree = None

        # compressed tree
        if f.lower().endswith('.tre.gz'):
            tree = gzip.open(directory + '/' + f,'rb').read().strip()

        # uncompressed tree
        elif f.lower().endswith('.tre'):
            tree = open(directory + '/' + f).read().strip()

        # add tree to file
        if tree != None:
            tree = re.sub('[0-9]+\.[0-9]+[Ee]-[0-9]+', sci_to_float, tree) # INDELible can't parse scientific notation
            name = f.lower().split('.tre')[0].strip()
            control += ("[TREE] " + name + ' ' + tree + '\n')
            trees.append(name)

    # write partitions
    control += "\n/* Partitions */\n"
    for name in trees:
        control += ('[PARTITIONS] p' + name + ' [' + name + ' GTRalu ' + str(length) + '] // create partition p' + name + ' with tree ' + name + ' under model GTRalu with root length = ' + str(length) + '\n')

    # evolve trees
    control += "\n/* Evolve Trees */\n[EVOLVE]\n"
    for name in trees:
        control += ("    p" + name + ' ' + str(reps) + ' ' + name + ' // evolve partition p' + name + ' for ' + str(reps) + ' rep and output seqs as ' + name + '.fas\n')

    # return control file as string
    return control

# if code is executed (and not imported) # UPDATE THIS!!!!
if __name__ == '__main__':
    # parse args
    if len(sys.argv) != 7:
        print("ERROR: Incorrect number of arguments")
        print(USAGE_MESSAGE)
        exit(-1)
    directory = sys.argv[1].strip()
    if not os.path.isdir(directory):
        print("ERROR: Specified directory does not exist (" + directory + ")")
        print(USAGE_MESSAGE)
        exit(-1)
    try:
        length = int(sys.argv[2])
    except:
        print("ERROR: Specified length is not an integer (" + sys.argv[2] + ")")
        print(USAGE_MESSAGE)
        exit(-1)
    try:
        reps = int(sys.argv[3])
    except:
        print("ERROR: Specified number of repititions is not an integer (" + sys.argv[3] + ")")
    try:
        pA,pC,pG,pT = [float(i) for i in sys.argv[4].strip().split(',')]
    except:
        print("ERROR: GTR State Frequencies are formatted incorrectly")
        print(USAGE_MESSAGE)
        exit(-1)
    try:
        pAC,pAG,pAT,pCG,pCT,pGT = [float(i) for i in sys.argv[5].strip().split(',')]
    except:
        print("ERROR: GTR Substitution Rates are formatted incorrectly")
        print(USAGE_MESSAGE)
        exit(-1)
    try:
        alpha = float(sys.argv[6])
    except:
        print("ERROR: Gamma distribution alpha parameter is not a float (" + sys.argv[6] + ")")
        print(USAGE_MESSAGE)
        exit(-1)

    # generate INDELible control file and write to disk
    control = generateControl(directory,length,reps,pA,pC,pG,pT,pAC,pAG,pAT,pCG,pCT,pGT,alpha)
    open(directory + '/control.txt','w').write(control)
    print("Successfully wrote " + directory + "/control.txt")