#!/usr/bin/env python

import sys
import numpy as np

fa=sys.argv[1]
outfile=sys.argv[2]

file = open(fa,'r')
output = open(outfile,'w')

current_name =""
max_name=""
maximal = 0
max_string=""
lst=[]
hash_line={}

for line in file:
    if line.startswith(">"):
        lst.append(line)
        current_name=line
    else:
        if current_name not in hash_line.keys():
            hash_line[current_name] = line.strip("\n")
        else:
            hash_line[current_name]+=line.strip("\n")
            
for key in hash_line:
    if len(hash_line[key]) > maximal:
        maximal = len(hash_line[key])
        
        max_name = key
        max_string = hash_line[key]
         
output.write(max_name)

partition = np.ceil(len(max_string)/60)
for idx in range(0,int(partition)):
    sequence=max_string[60*idx:60*(idx+1)]
    output.write(sequence+'\n')

file.close()
output.close()
