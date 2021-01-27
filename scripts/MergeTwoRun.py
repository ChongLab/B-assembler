#!/usr/bin/env python

import os,sys
import pandas as pd
import numpy as np

paf = sys.argv[1]
firstrun = sys.argv[2]
secondrun = sys.argv[3]
outfile = sys.argv[4]

##transfer firstrun and secondrun contig to single line
with open(firstrun) as f_input, open('output/firstrun_single', 'w') as f_output:
    block = []
    for line in f_input:
        if line.startswith('>'):
            if block:
                f_output.write(''.join(block) + '\n')
                block = []
        else:
            block.append(line.strip())
    if block:
        f_output.write(''.join(block) + '\n')

## merge two round 
output=open(outfile, 'w')
alin=open(paf,'r')
seqfile=open(secondrun, 'r')
firstrunSeq=open('output/firstrun_single', 'r').read() 
str_1=()
str_2=()
contig_1=()
contig_2=()
df = pd.read_csv(alin, sep="\t", header=None)
str_1=df.iloc[df[7].idxmin()]
str_2=df.iloc[df[8].idxmax()]
contig_1=str_1[0]
contig_2=str_2[0]
#if str_1[2]>str_2[2]:
cutPoint_1=str_1[2]
cutPoint_2=str_1[3]
cutPoint_3=str_2[2]
cutPoint_4=str_2[3]
cutPoint_5=str_1[8]
cutPoint_6=str_2[7]
seqThree=firstrunSeq[cutPoint_5:cutPoint_6]

if contig_1==contig_2:
    for line in seqfile:
        if line.startswith('>'+contig_1):
            seq=next(seqfile, '').strip()
            seqOne=seq[cutPoint_1:cutPoint_2]
            seqTwo=seq[cutPoint_3:cutPoint_4]
    if str_1[2]>str_2[2]:
        
        wholeSeq=seqTwo+seqThree+seqOne
    else:
        wholeSeq=seqOne+seqThree+seqTwo
else:
    for line in seqfile:
        if line.startswith('>'+contig_1):
            seq_1=next(seqfile, '').strip()
            seqOne=seq_1[cutPoint_1:cutPoint_2]
        elif line.startswith('>'+contig_2):
            seq_2=next(seqfile, '').strip()
            seqTwo=seq_2[cutPoint_3:cutPoint_4]
    wholeSeq=seqOne+seqThree+seqTwo

output.write(">merge_firstrun_secondrun\n")
partition = np.ceil(len(wholeSeq)/60)
for idx in range(0,int(partition)):
    sequence=wholeSeq[60*idx:60*(idx+1)]
    output.write(sequence + "\n")

print(len(wholeSeq))
    
alin.close()
seqfile.close()
output.close()
