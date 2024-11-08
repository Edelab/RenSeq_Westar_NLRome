# sequence alignment by using MUSCLE  
/path/to/muscle5.1.linux_intel64 -align TCRNL_nbarc.fasta -output NBARC_align.fasta

# trimming by using Clipkit  
clipkit NBARC_align.fasta -m gappy -s aa

# command for MLtree by using IQ-TREE2  
iqtree2 -s NBARC_align_clipkit.fasta -m MFP -bb 1000 -bnni -redo -ntmax 30
