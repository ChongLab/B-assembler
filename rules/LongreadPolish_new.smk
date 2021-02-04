#choose Read type ONT or pacbio
par=""
readType=config['readtype']
if readType=="ONT":
    par="--nano-raw"
else:
    par="--pacbio-raw"

rule polish_round1:
    input:
        assembly="output/firstrun.fa",
        read=config['longread']
    output:
        "output/polished_1.fasta"
    params:
        dir="output/",
        type=par

    shell:
        """
        flye --polish-target {input.assembly} {params.type} {input.read} --iterations 2 --out-dir {params.dir} 
        """

rule rename:
    input:
        "output/polished_1.fasta"
    output:
        "output/B_assembly.fasta"
    shell:
        """
        mv {input} {output}
        """
