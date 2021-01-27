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

