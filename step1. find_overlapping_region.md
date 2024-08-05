#download the Westar genome and annotation file from BNIR    
wget https://yanglab.hzau.edu.cn/static/bnir/assets//genomic_sequence/BnIRData/AACC.Brassica_napus/Westar/v0/Brassica_napus.Westar.v0.genome.fa.gz  

wget https://yanglab.hzau.edu.cn/static/bnir/assets//genomic_sequence/BnIRData/AACC.Brassica_napus/Westar/v0/Brassica_napus.Westar.v0.gene.gff3.gz

#using bwa-mem2 to map the Renseq reads on Westar genome    

./bwa-mem2 index /path/to/Brassica_napus.Westar.v0.genome.fa.gz    
./bwa-mem2 mem -t 30 <prefix> <reads.fq/fa> > westar.sam    

#use samtools to covert the sam file to bam file and sort
samtools views -S path/to/westar.sam -b -o westar.bam  
samtools sort westar.bam -@ 20 -o sorted.bam

#calculate the coverage of the renseq reads

samtools depth sorted.bam > coverage.txt    

#filter the coverage higher than 50 times    

awk '{ if ($3 > 50) print $1"\t"$2-1"\t"$2 }' coverage.txt > 50high_coverage.bed    

#filter the sequence at least 1kb region    

bedtools merge -i 50high_coverage.bed -d 0 -c 1 -o count_distinct | awk '$3-$2 >= 1000' > final_regions.bed    

#grep the genes from the reference annotation file from the regions we filtered before    

awk 'BEGIN{OFS="\t"}{print $1, "Extracted", "region", $2, $3, ".", ".", ".", "ID=region"$1"_"$2"_"$3}' final_regions.bed > final_regions.gff    

grep -w 'gene' /path/to/Brassica_napus.Westar.v0.gene.gff3 > genes_only.gff    

awk 'BEGIN{OFS="\t"}{if($3=="gene") print $1,$4-1,$5,$9}' genes_only.gff > genes_only.bed    

awk 'BEGIN{OFS="\t"}{if($3=="region") print $1,$4-1,$5,$9}' final_regions.gff > renseq_regions.bed    

#use bedtools to find the overlapping RenSeq regions, "NLR-Annotator" and reference annotation from these regions    

bedtools intersect -a renseq_regions.bed -b genes_only.bed westar_nlr.bed -wo -f 0.1 > overlaps.bed   

cut -f 4 overlaps.bed > overlapping_ids.txt    
