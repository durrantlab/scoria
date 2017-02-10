# NEVER MIND THIS FILE FOR NOW. MDANALYSIS CONSTRUCTOR STILL BEING CREATED...

import scoria

#mol = scoria.Molecule()
#mol.load_pdb_into("scoria/sample-files/single_frame.pdb", False, False, False)
#print mol.information.get_trajectory_frame_count()

# Load PSF and DCD files.
#mol = scoria.Molecule()
#mol.load_via_MDAnalysis("./scoria/sample-files/M2_traj.psf", "./scoria/sample-files/M2_traj.dcd")

#print mol.save_pdb("test.pdb")

mol = scoria.Molecule()
#mol.load_pdb_into("test.pdb", is_trajectory = True)

#mol.fileio.load_pdb_trajectory_into("test.pdb")
mol.fileio.load_pdbqt_trajectory_into("scoria/sample-files/vina.out")
#mol.load_pdbqt_into("scoria/sample-files/vina.out", is_trajectory = True)

#print mol.information.get_trajectory_frame_count()
#print mol.information.__trajectory
#print list(mol.get_coordinates())

import pdb; pdb.set_trace()