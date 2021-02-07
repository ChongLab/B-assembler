import os
directory="output"
if not os.path.exists(directory):
    os.makedirs(directory)
directory="output/secondrun"
if not os.path.exists(directory):
    os.makedirs(directory)

rule select_longread:
    input:
        raw=config['longread']
    output:
        long="output/filter_length.fq",
        short="output/left_filter_length.fq"
    params:
        config['genomesize']
    shell:
        """
        python scripts/SelectLongRead.py {input.raw} {params} {output.long} {output.short}
        """
rule fq_to_fa:
    input:
        "output/filter_length.fq"
    output:
        "output/filter_length.fa"
    shell:
        """
        python scripts/FqToFa.py {input} {output}
        """
##longRead_correct
par=""
readType=config['readtype']
if readType=="ONT":
    par="map-ont"
else:
    par="map-pb"

rule short_to_long:
    input:
        long = "output/filter_length.fa",
        short = "output/left_filter_length.fq"
    output:
        "output/short_to_long.sam"
    params:
        type=par
    shell:
        """
        minimap2 -ax {params.type} {input.long} {input.short} > {output}
        """
rule longread_polish:
    input:
        long = 'output/filter_length.fa',
        short = 'output/left_filter_length.fq',
        sam = 'output/short_to_long.sam'
    output:
        "output/long_read_corrected.fasta"
    shell:
        """
        racon {input.short} {input.sam} {input.long} > {output}
        """
