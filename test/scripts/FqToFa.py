#!/usr/bin/env python

import sys, subprocess

infile = sys.argv[1]
fasta = sys.argv[2]
fastq = open(infile, 'r')

## main function, skip line id 34 and rest counter to write out the fasta
def main(fastq, fasta):
    line_n =0
    line_buffer = 0
    line_id = 1
    outfile = open(fasta, 'w')
    fastas = 1
    fasta_length =0
    for line in fastq:
        line_n += 1
	#line_id += 1
        if line_n == 10000:
            line_buffer += 10000
            line_n =0
        if line_id == 4:
            line_id = 1
        elif line_id == 3:
            line_id += 1
        elif line_id == 2:
            line_id += 1
            fasta_line = line
            fasta_length += len(fasta_line.strip())
            outfile.write(fasta_line)
            fastas += 1
        else:
            if '@' not in line:
                print('are you sure this is a fastq ??')
            else:
                fasta_header = line.replace('@', '>')
                line_id += 1
                outfile.write(fasta_header)
    outfile.close()
    print ('FASTA records written', fastas, 'average length of fasta sequences ', float(fasta_length//fastas))
if __name__ == '__main__':
    main(fastq, fasta)
fastq.close()
