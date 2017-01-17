import scoria

mol = scoria.Molecule()
mol.load_pdb_into("test.pdb", False, False, False, False)

mol.save_pdb("testttt.pdb")
