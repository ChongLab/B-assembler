rule tworun_align:
    input:
        sec="output/secondrun/assembly.fasta",
        fir="output/firstrun.fa"
    output:
        "output/first_second.paf"
    shell:
        """
        minimap2 -cx asm20 {input.fir} {input.sec} > {output}
        """
rule merge:
    input:
        paf="output/first_second.paf",
        first="output/firstrun.fa",
        second="output/secondrunOneline.fa"
    output:
        merge="output/First_second_merge.fa"
    shell:
        """
        python scripts/MergeTwoRun.py {input.paf} {input.first} {input.second} {output.merge}
        """
