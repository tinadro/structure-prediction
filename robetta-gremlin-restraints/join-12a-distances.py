import pandas as pd 

def joiner(mod):
	f1 = 'CjPflA-model'+mod+'-12a-dist.txt' # list of i, j residues that are in contact
	f2 = 'CjPflA-model'+mod+'-dist-measured.txt' # list of distances between i and j 
	df1 = pd.read_csv(f1, header=None, sep='\t')
	df2 = pd.read_csv(f2, header=None)
	print(len(df1), len(df2))
	df1[3] = df2[0]
	print(df1.head())
	df1.to_csv('contact-points-distance-measurements-model'+mod+'.tsv', sep='\t', header=None, index=None)

for i in range(1,6):
	joiner(str(i))
