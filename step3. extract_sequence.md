#use samtools to index referene genome    

samtools faidx /path/to/Brassica_napus.Westar.v0.genome.fa

#extract the RenSeq regions the with unique regions and add 1k left and right flanking regions    

cut -f 1,2 Brassica_napus.Westar.v0.genome.fa.fai > westar.genome.len   

bedtools slop -i filtered_gff_file.gff -g westar.genome.len -b 1000 > filtered_sequences_1kbflank.bed   

bedtools getfasta -fi /path/to/Brassica_napus.Westar.v0.genome.fa -bed filtered_sequences_1kflank.bed -fo filtered_sequences_1kflank.fasta
