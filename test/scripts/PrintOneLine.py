#!/usr/bin/env python

import sys

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile) as f_input, open(outfile, 'w') as f_output:
    block = []
    for line in f_input:
        if line.startswith('>'):
            if block:
                f_output.write(''.join(block) + '\n')
                block = []
            f_output.write(line)
        else:
            block.append(line.strip())
    if block:
        f_output.write(''.join(block) + '\n')
