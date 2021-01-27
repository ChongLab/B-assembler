#!/usr/bin/python

import os,sys 

rawrd = sys.argv[1]
len_distr = sys.argv[2]
genomeSize = sys.argv[3]
outfile = sys.argv[4]
outfile_2 = sys.argv[5]

#find the appropriate read length (reads longer than it had coverage 50)
file=open(len_distr,'r')
n=0
rd_sum=0

for line in file:
    n+=1
    line=line.strip('\n')
    rd_sum+=int(line)
    #print(rd_sum)
    if rd_sum/int(genomeSize) > 50:
        break
    rd_line=n

for line_no, line in enumerate(file): 
    if line_no == rd_line:
        rd_len=line

#filter reads that longer than selected length
fqfile=open(rawrd,'r')
fqfilter=open(outfile,'w')
leftfilter=open(outfile_2,'w')
i=0

for line in fqfile:
        #print i,i%4,line
    if i%4==0:
        seqID=line.strip("\n")
    elif i%4==1:
        sequence=line.strip("\n")
    elif i%4==2:
        mark=line.strip("\n")
    elif i%4==3:
        if len(sequence)>=int(rd_len):
            qual=line.strip("\n")
            fqfilter.write(seqID+"\n"+sequence+"\n"+mark+"\n"+qual+"\n")
        else: 
            qual=line.strip("\n")
            leftfilter.write(seqID+"\n"+sequence+"\n"+mark+"\n"+qual+"\n")
    i+=1

fqfile.close()
fqfilter.close()
leftfilter.close()
file.close()

