rule bwa_1:
    input:
        long = "output/First_second_merge.fa",
        short_1 = config['illumina']['R1'],
        short_2 = config['illumina']['R2']
    output:
        bam="output/short_merge_srt_1.bam",
        bai="output/short_merge_srt_1.bam.bai"
    conda:
        'envs/bwa.yaml'
    shell:
        """
        bwa index {input.long};
        bwa mem -t 8 {input.long} {input.short_1} {input.short_2} |samtools view -Sb - | samtools sort - -o {output.bam};
        samtools index {output.bam}
        """

rule pilon_polish_1:
    input:
        long = 'output/First_second_merge.fa',
        bam = 'output/short_merge_srt_1.bam'
    output:
        "output/merge_pilon_corrected_1.fasta"
    params:
        output_prefix = 'merge_pilon_corrected_1',
        output_dir = 'output'
    shell:
        """
        java -Xmx10G -jar script/pilon-1.23.jar --genome {input.long} --frags {input.bam} --fix all --output {params.output_prefix} --outdir {params.output_dir} 
        """
rule bwa_2:
    input:
        long = "output/merge_pilon_corrected_1.fasta",
        short_1 = config['illumina']['R1'],
        short_2 = config['illumina']['R2']
    output:
        bam="output/short_merge_srt_2.bam",
        bai="output/short_merge_srt_2.bam.bai"
    conda:
        'envs/bwa.yaml'
    shell:
        """
        bwa index {input.long};
        bwa mem -t 8 {input.long} {input.short_1} {input.short_2} |samtools view -Sb - | samtools sort - -o {output.bam};
        samtools index {output.bam}
        """
rule pilon_polish_2:
    input:
        long = 'output/merge_pilon_corrected_1.fasta',
        bam = 'output/short_merge_srt_2.bam'
    output:
        "output/merge_pilon_corrected_2.fasta"
    params:
        output_prefix = 'merge_pilon_corrected_2',
        output_dir = 'output'
    shell:
        """
        java -Xmx10G -jar script/pilon-1.23.jar --genome {input.long} --frags {input.bam} --fix all --output {params.output_prefix} --outdir {params.output_dir}
        """
rule bwa_3:
    input:
        long = "output/merge_pilon_corrected_2.fasta",
        short_1 = config['illumina']['R1'],
        short_2 = config['illumina']['R2']
    output:
        bam="output/short_merge_srt_3.bam",
        bai="output/short_merge_srt_3.bam.bai"
    conda:
        'envs/bwa.yaml'
    shell:
        """
        bwa index {input.long};
        bwa mem -t 8 {input.long} {input.short_1} {input.short_2} |samtools view -Sb - | samtools sort - -o {output.bam};
        samtools index {output.bam}
        """
rule pilon_polish_3:
    input:
        long = 'output/merge_pilon_corrected_2.fasta',
        bam = 'output/short_merge_srt_3.bam'
    output:
        "output/merge_pilon_corrected_3.fasta"
    params:
        output_prefix = 'merge_pilon_corrected_3',
        output_dir = 'output'
    shell:
        """
        java -Xmx10G -jar script/pilon-1.23.jar --genome {input.long} --frags {input.bam} --fix all --output {params.output_prefix} --outdir {params.output_dir}
        """
rule bwa_4:
    input:
        long = "output/merge_pilon_corrected_3.fasta",
        short_1 = config['illumina']['R1'],
        short_2 = config['illumina']['R2']
    output:
        bam="output/short_merge_srt_4.bam",
        bai="output/short_merge_srt_4.bam.bai"
    conda:
        'envs/bwa.yaml'
    shell:
        """
        bwa index {input.long};
        bwa mem -t 8 {input.long} {input.short_1} {input.short_2} |samtools view -Sb - | samtools sort - -o {output.bam};
        samtools index {output.bam}
        """ 

rule pilon_polish_4:
    input:
        long = 'output/merge_pilon_corrected_3.fasta',
        bam = 'output/short_merge_srt_4.bam'
    output:
        "output/merge_corrected_4.fasta"
    params:
        output_prefix = 'merge_corrected_4',
        output_dir = 'output'
    shell:
        """
        java -Xmx10G -jar script/pilon-1.23.jar --genome {input.long} --frags {input.bam} --fix all --output {params.output_prefix} --outdir {params.output_dir}
        """
