#!/usr/bin/env python

import sys,subprocess
import pandas as pd
import numpy as np

fa=sys.argv[1]
queryRead=sys.argv[2]
outfile=sys.argv[3]

##balst sequence with dnaA gene
cmd = 'makeblastdb -in '+str(fa)+' -dbtype nucl -out output/blast && tblastn -db output/blast -query '+str(queryRead)+' -outfmt 7 -out output/query.txt'
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
t = p.communicate()[0].decode('utf-8')

##rearrange sequence by the alignment
file = open(fa,'r')
current_string=""
for line in file:
    if line.startswith("A") or line.startswith("T") or line.startswith("C") or line.startswith("G"):
        current_string+=line.strip("\n")
Tlen=len(current_string)

##find the besthit, select the smallest evalue,in case of identical E-values, the bit score is used as secondary ranking criterion
df = pd.read_csv("output/query.txt",sep="\t",error_bad_lines=False, keep_default_na=False,comment='#',header=None)
besthit=[]
df= df.sort_values(by=11,ascending=False)
df = df.sort_values(by=10)
df_fliter=df[2]>=50
filtered_df = df[df_fliter]
besthit=filtered_df.head(10)
sstart= besthit.iloc[0].at[8]
send= besthit.iloc[0].at[9]

if sstart>send:
    FirstPart=current_string[0:sstart]
    FirstPart_rev=FirstPart[::-1]
    EndPart=current_string[sstart+1:Tlen]
    EndPart_rev=EndPart[::-1]
    whole_sequence=FirstPart_rev+EndPart_rev
else:
    FirstPart=current_string[sstart:Tlen]
    EndPart=current_string[0:sstart-1]
    whole_sequence=FirstPart+EndPart
        
output = open(outfile, 'w')
output.write(">merge_firstrun_secondrun\n")
partition = np.ceil(len(whole_sequence)/60)
for idx in range(0,int(partition)):
    sequence=whole_sequence[60*idx:60*(idx+1)]
    output.write(sequence+"\n")

file.close()
output.close()
