for line in f:
import scoria as pymol

mol = pymol.Molecule("PDB","scoria/sample-files/single_frame.pdb")
sel = {"bad":"thing"}
mol.select_atoms(sel)
