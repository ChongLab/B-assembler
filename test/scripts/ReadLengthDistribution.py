#!/usr/bin/env python

import sys

fastq_file = open(sys.argv[1], 'r')
prefix = sys.argv[1].split('.')[0]
outfile = open('output/read_length_distrbution_notSort.txt', 'w')
seq = ''
for line in fastq_file:
    line = line.rstrip('\n')
    if line.startswith('@'):
        if seq:
            outfile.write(str(len(seq)) + '\n')
            seq = ""
        name = line 
    else:
        seq = line 
outfile.write(str(len(seq)) + '\n')

outfile.close()
fastq_file.close()
print ('\n' + '\t' + 'File: ' + 'lenghts.txt has been created...')

##sort length by value
infile=open("output/read_length_distrbution_notSort.txt", 'r')
len_dis=open(sys.argv[2], 'w')

ls=[]
for line in infile:
    line=line.strip('\n')
    ls.append(line)
for i in range(0, len(ls)):
    ls[i] = int(ls[i]) 
ls.sort(reverse=True) 
for ele in ls:
    len_dis.write(str(ele) + '\n')

infile.close()
len_dis.close()
