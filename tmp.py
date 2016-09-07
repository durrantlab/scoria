import pymolecule

m = pymolecule.Molecule()
m.load_pdb_into("examp2.pdb")
m.save_pdb("tmp.pdb")