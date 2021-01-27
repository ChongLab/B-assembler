<p align="center"><img alt="B-assembler" width="600"></p>
B-assembler is a snakemake-based pipeline for assembling bacterial genomes from long reads (nanopore or pacbio) or hybrid reads (long and short reads)

# Introduction
As input, B-assembler takes one of the following:
* A set of long reads (Nanopore or pacbio) from a bacterial isolate (uncorrected long reads are fine, though corrected long reads should work too)
* Illumina reads from a bacterial isolate (required paired-end reads) and long reads from the same isolate (best case)

Reasons to use B-assembler:
* It is a best-practice for long reads bioinformatics into a (hopefully) easy-to-use pipeline, taking advantage of all the goodness of Snakemake while adding a few features; including:
  * a text-based read config that allows automated simple read pre-processing (select reads based on read length)
  * a text-based run config that provides a trivial way to define assembly and polishing strategies (long read only or hybrid read mode)
  * automatic generation of assembly 
* It circularises genome without the need for a separate tool like Circlator.
* It can use long reads or hybrid reads in hybrid assembly.
* It has very low misassembly rates.
* It's easy to use: runs with just one command and usually doesn't require tinkering with parameters.
* It is fast. Running time just need few hours.

Reasons to __not__ use B-assembler:
* You're assembling a eukaryotic genome or a metagenome (Pipeline is designed exclusively for bacterial isolates).
* Your long reads are low depth (<50).
* Your Illumina reads and long reads are from different isolates.
* only Illumina reads.

# Requirements
* Linux or macOS
* B-assembler base on conda, the environments include snakemake are installed by conda, conda:https://conda.io/projects/conda/en/latest/user-guide/install/linux.html 
* [Python](https://www.python.org/) 3.6 or later
* Environments of conda installed tools
  * Flye v2.7 (https://github.com/fenderglass/Flye)
  * Racon (https://github.com/isovic/racon)
  * BWA mem (https://sourceforge.net/projects/bio-bwa/files/)
  * Pilon (pilon1.23.jar) (https://github.com/broadinstitute/pilon)
  * Samtools v1.0 or later (https://sourceforge.net/projects/samtools/files/samtools/)
  * Minimap2 v2.1 (https://github.com/lh3/minimap2)
  * blast (https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download)
# Installation

## Install from source

```
git clone https://github.com/huang1990/B-assembler.git; cd B-assembler;
```

## setup the environment

```
conda env create -n B-assembler -f env.yaml
conda activate B-assembler
```
**Note** It is important that you ensure all bioconda installed tools installed.

## Write your configuation
###Provide sequence data in config.yaml file
```
vi config.yaml
```

Replace the YAML keys as appropriate. Keys are:
| Key | Type | Description | 
|-----|------|-------------|
|`longread` | Path to Nanopore or Pacbio reads | It requires path to your long reads, pull all your reads into one fastq file, it is recommended to provide absolute path, you can ignore this if you do not have nanopore reads|
| `Illumina R1`| path to Illumina R1 | Read1 of paired-end Illumina reads, it is recommended to provide absolute path, you can ignore this if you do not have Illumina reads|
| `Illumina R2`| path to Illumina R2 | Read2 of paired-end Illumina reads, it is recommended to provide absolute path, you can ignore this if you do not have Illumina reads|
| `genomesize`| int | number of base pair of extimated genomesize of your species|
| `readtype`| ONT or pb | Type of your long reads, ONT is for nanopore, pb is for pacbio|
| `current pathway`| absolute path of B-assembler directary | start_gene.fa file is in B-assembler/script directary, it needsYour working path to rearrange start point|

## Engage the pipeline
Run the pipeline, you **must** specify `cores` to ensure that how many threads you give. 
##Usage
```
usage: bash run_B-assembler.sh <cores> <LongReadOnly/Hybrid>

Require arguments:
cores:int
         threads provided for pipeline
LongReadOnly/Hybrid
         assembly mode for your reads 
```
##Examples
```
bash run_B-assembler.sh 2 LongReadOnly
```
# output

The final assembly will be in the output directory, and the name of assembly: B-assembler.fasta

