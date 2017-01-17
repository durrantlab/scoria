for line in f:
import scoria as pymol

mol = pymol.Molecule("PDB","scoria/sample_files/single_frame.pdb")
sel = {"bad":"thing"}
mol.select_atoms(sel)
