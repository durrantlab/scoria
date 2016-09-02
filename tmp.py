import pymolecule

m = pymolecule.Molecule()
m.load_pdb_into("example.pdb")
m.save_pdb("tmp.pdb")