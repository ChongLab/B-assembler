#!/usr/bin/env python

import sys

infile= sys.argv[1]
file = open(infile, 'r')

def toONElineFASTA(file):
    'Convert multi-line fasta to one-line fasta'
    db = {}
    for line in file.readlines():
        if line.startswith('>'):
            keys = line.strip()
            db[keys] = []
        else:
            db[keys].append(line.strip())
    for ID, seq in db.items():
        print(''.join(seq))

toONElineFASTA(file)
file.close()
