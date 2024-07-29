import pandas as pd

# read gff files
gff_df = pd.read_csv('final_regions.gff', sep='\t', header=None, comment='#')
gff_df.columns = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']

# read the overlapping id file
id_df = pd.read_csv('overlapping_ids.txt', header=None)
id_df.columns = ['ID']

gff_df['extracted_id'] = gff_df['attribute'].apply(lambda x: 'ID=' + x.split('ID=')[1].split(';')[0] if 'ID=' in x else '')

# filter it
filtered_gff = gff_df[~gff_df['extracted_id'].isin(id_df['ID'])]

# save the file
filtered_gff.drop(columns='extracted_id').to_csv('filtered_gff_file.gff', sep='\t', index=False, header=False)
