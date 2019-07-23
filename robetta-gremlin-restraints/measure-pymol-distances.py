import csv
from pymol import cmd
import sys

with open('CjPflA-model5-12a-dist.txt', 'r') as f:
	pairs = [tuple(line[0].split('\t')) for line in csv.reader(f)]

print(pairs)

f = open('CjPflA-model5-dist-measured.txt', 'a+')

for i, j in pairs:
	dst=cmd.distance('tmp', '/CjPflA-model5-full//A/'+i+'/CA', '/CjPflA-model5-full//A/'+j+'/CA')
	f.write("%8.3f\n"%dst)

f.close()
