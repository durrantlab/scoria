#import pymolecule
#mol = pymolecule.Molecule()
#mol.load_pdb_into("test.pdb", False, False, False, False)

import numpy

f = open("test.pdb", "r")

data = []
for line in f:
    data.append((line[:6], line[6:11], line[11:16], line[16:21], line[21:22], line[22:26], line[26:30], line[30:38], line[38:46], line[46:54], line[54:60], line[60:66], line[66:76], line[76:78], line[78:81]))

s1 = ["|S6","|S5","|S5","|S5","|S1","|S4","|S4","|S8","|S8","|S8","|S6","|S6","|S10","|S2","|S3"]
names = ['record_name', 'serial', 'name', 'resname', 'chainid', 'resseq', 'empty', 'x', 'y', 'z', 'occupancy', 'tempfactor', 'empty2', 'element', 'charge']
dtype = [l for l in zip(names, s1)]

n = numpy.array(data, dtype=dtype)

print(n)

# dtype = "S6,S5,S5,S5,S1,S4,S4,S8,S8,S8,S6,S6,S10,S2,S3",
# [ ('REMARK', ' This', ' is a', ' rema', 'r', 'k.\n', '', '', '', '', '', '', '', '', '')
#  ('ATOM  ', '    1', '  N  ', ' GLN ', 'A', '  52', '    ', ' 542.237', '  16.800', '  35.823', '  1.00', ' 12.04', '          ', ' N', '  \n')
#  ('ATOM  ', '    2', '  CA ', ' GLN ', 'A', '  52', '    ', ' 541.667', '  17.015', '  34.477', '  1.00', ' 10.21', '          ', ' C', '  \n')
#  ('ATOM  ', '    3', '  C  ', ' GLN ', 'A', '  52', '    ', ' 540.148', '  17.010', '  34.446', '  1.00', ' 10.33', '          ', ' C', '  \n')
