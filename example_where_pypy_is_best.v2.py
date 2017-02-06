import scoria
from scoria import dumbpy as numpy
import time

t1 = time.time()

for t in range(50000000):
    pass

mol = scoria.Molecule()
mol.load_pdb_into("scoria/sample-files/single_frame.pdb", False, False, False, False)

print(time.time() - t1)
