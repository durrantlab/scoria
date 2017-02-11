import scoria
from scoria.dumbpy import array

mol = scoria.Molecule()
mol.load_pdb_into("test2.pdb", False, False, False, False)

mol2 = scoria.Molecule()
mol2.load_pdb_into("test2.pdb", False, False, False, False)

mol2.translate_molecule(array([5.0, 5.0,0]))

print mol.get_rmsd_order_dependent(mol2)

mol2.save_pdb("jj.pdb")
