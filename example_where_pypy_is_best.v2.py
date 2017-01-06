import pymolecule
from pymolecule import dumbpy as numpy
import time

t1 = time.time()

for t in range(50000000):
    pass

mol = pymolecule.Molecule()
mol.load_pdb_into("pymolecule/sample_files/single_frame.pdb", False, False, False, False)

print time.time() - t1
