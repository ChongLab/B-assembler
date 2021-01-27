#!/usr/bin/env python

import subprocess,sys

infile = sys.argv[1]
bam=sys.argv[2]
out_1=sys.argv[3]
out_2=sys.argv[4]
file = open(infile,'r')
current_string=""
current_name =""
for line in file:

    if line.startswith("A") or line.startswith("T") or line.startswith("C") or line.startswith("G"):
        current_string+=line.strip("\n")    
    if line.startswith(">"):
        current_name=line.strip("\n")

contig=current_name.replace(">", "")
endNum=len(current_string)
startNum=int(int(endNum) - int(endNum)*0.2)
beginNum=int(int(endNum)*0.2)

##reads select
cmd='samtools view -h '+str(bam)+' '+str(contig)+':'+str(startNum)+'-'+str(endNum)+' | samtools fastq - > '+str(out_2)+''
out3 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
out3_status = out3.wait()
cmd='samtools view -h '+str(bam)+' '+str(contig)+':1-'+str(beginNum)+' | samtools fastq - > '+str(out_1)+''
out4 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
out4_status = out4.wait()
file.close()
