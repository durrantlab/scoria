# NEVER MIND THIS FILE FOR NOW. MDANALYSIS CONSTRUCTOR STILL BEING CREATED...

import pymolecule

# Load PSF and DCD files.
mol = pymolecule.Molecule()
mol.load_via_MDAnalysis("./pymolecule/sample_files/M2_traj.psf", "./pymolecule/sample_files/M2_traj.dcd")

print list(mol.get_coordinates())

import pdb; pdb.set_trace()