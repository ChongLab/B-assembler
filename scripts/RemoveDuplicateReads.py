#!/usr/bin/env python

import sys

infile = sys.argv[1]
outfile = sys.argv[2]
holder=[]

with open(infile,'r') as file:
    rec=file.read().split('>')[1:]
    rec=['>'+i.strip() for i in rec]
holder.extend(rec)
total='\n'.join(list(set(holder)))
with open(outfile,'w') as out:
    out.write(total)
