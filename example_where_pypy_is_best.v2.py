from __future__ import absolute_import
from __future__ import print_function
import scoria
from scoria import dumbpy as numpy
import time
from six.moves import range

t1 = time.time()

for t in range(50000000):
    pass

mol = scoria.Molecule()
mol.load_pdb_into("scoria/sample-files/single_frame.pdb", False, False, False, False)

print((time.time() - t1))
