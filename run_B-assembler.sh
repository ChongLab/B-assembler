#!/bin/bash

if [ $# -lt 2 ] || [ $# -gt 3 ]; then

cat <<USAGE
Usage: bash $0 <numCPUs> <LongReadOnly|Hybrid> [output:PWD]

Require arguments:
numCPUs: int
         threads provided for pipeline

LongReadOnly|Hybrid
         assembly mode for your reads, type "LongReadOnly" or "Hybrid" based on your data

Optional argument:
output:
         output directory, current working directory by default
USAGE
fi

if [ $# -eq 3 ]; then
	mkdir $3
	cd $3;
	snakemake --cores $1 --snakefile $2
	cd -
fi

if [ $# -eq 2 ]; then
	snakemake --cores $1 --snakefile $2
fi
