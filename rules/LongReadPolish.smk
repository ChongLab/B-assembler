##decide read type to align
par=""
readType=config['readtype']
if readType=="ONT":
    par="map-ont"
else:
    par="map-pb"

rule polish_round1:
    input:
        assembly="output/First_second_merge.fa",
        read=config['longread']
    output:
        "output/racon_polish_1.fa"
    params:
        type=par
    shell:
        """
        minimap2 -ax {params.type} {input.assembly} {input.read} > output/rawfq_merged.sam && racon {input.read} output/rawfq_merged.sam {input.assembly} > {output}
        """
rule polish_round2:
    input:
        assembly="output/racon_polish_1.fa",
        read=config['longread']
    output:
        "output/racon_polish_2.fa"
    params:
        type=par
    shell:
        "minimap2 -ax {params.type} {input.assembly} {input.read} > output/rawfq_merged_2.sam && racon {input.read} output/rawfq_merged_2.sam {input.assembly} > {output}"

rule polish_round3:
    input:
        assembly="output/racon_polish_2.fa",
        read=config['longread']
    output:
        "output/racon_polish_3.fa"
    params:
        type=par
    shell:
        "minimap2 -ax {params.type} {input.assembly} {input.read} > output/rawfq_merged_3.sam && racon {input.read} output/rawfq_merged_3.sam {input.assembly} > {output}"

rule polish_round4:
    input:
        assembly="output/racon_polish_3.fa",
        read=config['longread']
    output:
        "output/merge_corrected_4.fasta"
    params:
        type=par
    shell:
        "minimap2 -ax {params.type} {input.assembly} {input.read} > output/rawfq_merged_4.sam && racon {input.read} output/rawfq_merged_4.sam {input.assembly} > {output}"


