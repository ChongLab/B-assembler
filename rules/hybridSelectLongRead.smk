rule longread_len:
    input:
        config['longread']
    output:
        "output/read_len_distrbution_2.txt"
    shell:
        "python scripts/ReadLengthDistribution.py {input} {output}"

rule select_longread:
    input:
        raw=config['longread'],
        lenDis="output/read_len_distrbution_2.txt",
    output:
        long="output/filter_length.fq",
        short="output/left_filter_length.fq"
    params:
        config['genomesize']
    shell:
        """
        python scripts/SelectLongRead.py {input.raw} {input.lenDis} {params} {output.long} {output.short}
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
rule bwa:
    input:
        long = "output/filter_length.fa",
        short_1 = config['illumina']['R1'],
        short_2 = config['illumina']['R2']
    output:
        bam="output/short_read_long-srt.bam",
        bai="output/short_read_long-srt.bam.bai"
    conda:
        'envs/bwa.yaml'
    shell:
        'bwa index {input.long};'
        'bwa mem -t 8 {input.long} {input.short_1} {input.short_2} | samtools view -Sb - |  samtools sort - -o {output.bam};'
        'samtools index {output.bam}'

rule longread_polish:
    input:
        long = 'output/filter_length.fa',
        bam = 'output/short_read_long-srt.bam'
    output:
        "output/long_read_corrected.fasta"
    params:
        output_prefix = 'long_read_corrected',
        output_dir = 'output'
    shell:
        """
        java -Xmx10G -jar script/pilon-1.23.jar --genome {input.long} --frags {input.bam} --fix all --output {params.output_prefix} --outdir {params.output_dir}
        """
