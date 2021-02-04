##select end reads for secondrun assembly
rule endReads_select:
    input:
        fa="output/firstrun.fa",
        bam="output/rawfq-firstrun-srt.bam",
        bai="output/rawfq-firstrun-srt.bam.bai"
    output:
        end="output/EndAlign.fq",
        begin="output/beginAlign.fq"
    shell:
        """
        python scripts/ExtractEndReads.py {input.fa} {input.bam} {output.begin} {output.end}
        """
rule merge_end_reads:
    input:
        "output/EndAlign.fq",
        "output/beginAlign.fq"
    output:
        Endfq="output/EndReads.fq",
        Endfa="output/EndReads.fa"
    shell:
        """
        cat {input} > {output.Endfq} && python scripts/FqToFa.py {output.Endfq} {output.Endfa}
        """
rule remove_dupl:
    input:
        "output/EndReads.fa"
    output:
        "output/EndReads_dupl_remove.fa"
    shell:
        """
        python scripts/RemoveDuplicateReads.py {input} {output}
        """
#secondrun assembly
par=""
readType=config['readtype']
if readType=="ONT":
    par="--nano-raw"
else:
    par="--pacbio-raw"
resize=int(int(config['genomesize'])*0.4)

rule second_assembly:
    input:
        "output/EndReads_dupl_remove.fa"
    output:
        "output/secondrun/assembly.fasta"
    params:
        dir="output/secondrun/",
        type=par,
        size=resize
    shell:
        """
        flye {params.type} {input} --min-overlap 3000 --genome-size {params.size} --out-dir {params.dir}
        """
rule select_longContig:
    input:
        "output/secondrun/assembly.fasta"
    output:
        "output/secondrunOneline.fa"
    shell:
        """
        python scripts/PrintOneLine.py {input} {output}
        """
