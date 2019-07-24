import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import matplotlib.colors as mcolors
import sys


#~~~~~~~~~~~~~~
# GET PDB DATA
#~~~~~~~~~~~~~~

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=-1):
	if n == -1:
		n = cmap.N
	new_cmap = mcolors.LinearSegmentedColormap.from_list('trunc({name},{a:.2f},{b:.2f})'.format(name=cmap.name, a=minval, b=maxval), cmap(np.linspace(minval, maxval, n)))
	return new_cmap

for nr in range(1, 6):
	data = pd.read_csv('CjPflB/contact-points-distance-measurements-model'+str(nr)+'.tsv', sep='\t', names=['i', 'j', 'dist'])
	data = data[data['dist'] < 8]
	data = data.sort_values('dist', ascending=False)

	x =  data['i'].tolist() + data['j'].tolist()
	y = data['j'].tolist() + data['i'].tolist()

	#make empty square matrix of dimensions = protein length 
	mtx = np.empty((821, 821))
	mtx.fill(np.nan)

	for ind, row in data.iterrows():
		i = int(row['i'])
		j = int(row['j'])
		s = row['dist']
		mtx[i,j] = s
		mtx[j,i] = s
	mx = max(data['dist'].tolist())
	mn = min(data['dist'].tolist())
	s = [((10-.001)*((x-mn)/(mx-mn)))+.001 for x in data['dist']]

	# TPR data : 
	tpr1 = range(177, 210)
	tpr2 = range(211, 244)
	tpr3 = range(310, 343)
	tpr4 = range(344, 377)
	tpr5 = range(465, 498)
	tpr6 = range(499, 532)
	tpra = range(709, 742)
	tprb = range(744, 777)
	tprc = range(778, 811)


	#~~~~~~~~~~
	# PLOTTING
	#~~~~~~~~~~

	cp = truncate_colormap(plt.get_cmap('winter'), 0.2, 1)

	fig, ax = plt.subplots()
	abc = plt.scatter(x, y, marker='.', s=s, c=mtx[x,y], cmap=cp)

	plt.scatter(tpr1, tpr1, marker='.', color='deeppink', s=2)
	plt.scatter(tpr2, tpr2, marker='.', color='deeppink', s=2)
	plt.scatter(tpr3, tpr3, marker='.', color='deeppink', s=2)
	plt.scatter(tpr4, tpr4, marker='.', color='deeppink', s=2)
	plt.scatter(tpr5, tpr5, marker='.', color='deeppink', s=2)
	plt.scatter(tpr6, tpr6, marker='.', color='deeppink', s=2)
	plt.scatter(tpra, tpra, marker='.', color='deeppink', s=2)
	plt.scatter(tprb, tprb, marker='.', color='deeppink', s=2)
	plt.scatter(tprc, tprc, marker='.', color='deeppink', s=2)

	plt.colorbar(abc)

	ax.xaxis.set_minor_locator(AutoMinorLocator(n=5))
	ax.yaxis.set_minor_locator(AutoMinorLocator(n=5))
	ax.yaxis.grid(b=True, which='major', linestyle='-')
	ax.yaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
	ax.xaxis.grid(b=True, which='major', linestyle='-')
	ax.xaxis.grid(b=True, which='minor', linestyle='-', color='0.9')
	ax.set_axisbelow(True)

	plt.ylim(820, 0)
	plt.xlim(0, 820)
	ax.set_aspect(820/820)
	plt.tight_layout()
	plt.savefig('contact-plots/CjPflB-contact-plot-model'+str(nr)+'-8a', dpi=300)
	plt.show()
