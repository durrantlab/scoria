# NEVER MIND THIS FILE FOR NOW. MDANALYSIS CONSTRUCTOR STILL BEING CREATED...

import pymolecule

#mol = pymolecule.Molecule()
#mol.load_pdb_into("pymolecule/sample_files/single_frame.pdb", False, False, False)
#print mol.information.get_trajectory_frame_count()

# Load PSF and DCD files.
mol = pymolecule.Molecule()
mol.load_via_MDAnalysis("./pymolecule/sample_files/M2_traj.psf", "./pymolecule/sample_files/M2_traj.dcd")

print mol.save_pdb("test.pdb")


#print mol.information.get_trajectory_frame_count()
#print mol.information.__trajectory
#print list(mol.get_coordinates())

#import pdb; pdb.set_trace()