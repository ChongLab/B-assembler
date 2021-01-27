#!/usr/bin/env python

import sys
import numpy as np

infile1=sys.argv[1]
infile2=sys.argv[2]
outfile=sys.argv[3]
file1 = open(infile1,'r')
strlist1=()

for line in file1:
    strlist1 = line

file2 = open(infile2,'r')
strlist2=()

for line in file2:
    strlist2 = line

strlist = strlist1 + strlist2
output = open(outfile, 'w')
output.write(">merge_firstrun_secondrun\n")
partition = np.ceil(len(strlist)/60)
for idx in range(0,int(partition)):
    sequence=strlist[60*idx:60*(idx+1)]
    output.write(sequence)

file1.close()
file2.close()
output.close()
