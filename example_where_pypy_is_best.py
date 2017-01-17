import scoria
from scoria import dumbpy as numpy
import time

t1 = time.time()


mol = scoria.Molecule()
mol.load_pdb_into("scoria/sample_files/single_frame.pdb", False, False, False, False)

for t in range(500):
    mol.translate_molecule(numpy.array([1.0, 0.0, 0.0]))
    mol.save_pdb("test.pdb")
    
print(time.time() - t1)
