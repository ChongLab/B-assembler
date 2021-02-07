#!/usr/bin/python

import os,sys 

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
len_dis=open("output/read_len_distrbution_2.txt", 'w')

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

rawrd = sys.argv[1]
genomeSize = sys.argv[2]
outfile = sys.argv[3]
outfile_2 = sys.argv[4]
#find the appropriate read length (reads longer than it had coverage 50)
file=open("output/read_len_distrbution_2.txt",'r')
n=0
rd_sum=0
rd_len=""

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
        if len(sequence)>=int(float(rd_len)):
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

