import os
import os.path
import glob

from pymol import cmd
from pymol import stored
from pymol import selector

files = glob.glob("*.pdb")
print(files)

for file in files:
        pdbName = os.path.basename(file).split(".")[0]
        cmd.load(file, pdbName)
        outFile = open(pdbName + '.ss', 'w+')
        stored.ss = ""
        cmd.iterate( '(n. CA)', 'stored.ss = stored.ss + ("%1s"%ss)')
        for c in stored.ss:
                if c  == " ":
                        outFile.write('.')
                else:
                        outFile.write(c)
        cmd.delete(pdbName)
        outFile.close()
