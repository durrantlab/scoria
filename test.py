import pymolecule as pymol

mol = pymol.Molecule("PDB","pymolecule/sample_files/single_frame.pdb")
sel = {"bad":"thing"}
mol.select_atoms(sel)
