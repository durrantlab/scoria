import pymolecule
from pymolecule import dumbpy as numpy
import time

t1 = time.time()


mol = pymolecule.Molecule()
mol.load_pdb_into("pymolecule/sample_files/single_frame.pdb", False, False, False, False)

for t in range(500):
    mol.translate_molecule(numpy.array([1.0, 0.0, 0.0]))
    mol.save_pdb("test.pdb")
    
print(time.time() - t1)
