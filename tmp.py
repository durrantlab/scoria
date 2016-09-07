import pymolecule
import glob

files = glob.glob("./pdb_examples/poses/vina.out_ligand_*pdbqt")
files.sort()



m1 = pymolecule.Molecule()
m1.load_pdbqt_into(files[0])

for t in files[1:]:
    m2 = pymolecule.Molecule()
    m2.load_pdbqt_into(t)
    print m1.get_rmsd_heuristic(m2)

#print m.get_atom_information().keys()
#for t in m.get_atom_information(): print t
# m.save_pdb("tmp.pdb")