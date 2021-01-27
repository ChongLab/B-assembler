rule rearrange:
    input:
        assembly="output/merge_corrected_4.fasta",
        startfa=config['dnAGene']
    output:
        "output/B_assembly.fasta"
    shell:
        """
        python scripts/RearrangeStartPoint.py {input.assembly} {input.startfa} {output}
        """
