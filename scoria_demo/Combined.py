import scoria
import numpy as np

# Load in a DCD/PSF trajectory.
print("Loading Molecule...")
mol = scoria.Molecule()
mol.load_MDAnalysis_into(
    "../scoria/sample-files/test_sim.psf", 
    "../scoria/sample-files/test_sim.dcd"
)

# Create two new trajectories, corresponding to the shroom2
# protein and the rock1 dimer, respectively. Shroom2 is 
# resid 1 to 181, and the rock1 dimer is 182 to 297.
print("Splitting trajectory into shroom2 and",)
print("rock1...")
shroom2 = mol.get_molecule_from_selection(
    mol.select_atoms({
        "resseq": range(1, 181)
    })
)
rock1 = mol.get_molecule_from_selection(
    mol.select_atoms({
        "resseq": range(182, 297)
    })
)

# Create numpy arrays to store the number of times each
# atom of shroom2 comes within 3.0 A of the atoms of rock1,
# and vice versa.
print("Calculating contacts...")
shroom2_counts = np.zeros(
    shroom2.get_total_number_of_atoms()
)
rock1_counts = np.zeros(
    rock1.get_total_number_of_atoms()
)

# Go through each frame and compare shroom2 and rock1
# atoms, keeping track of close-contact counts.
traj_length = mol.get_trajectory_frame_count()
for frame in range(0, traj_length):
    # Set the current trajectoyr frame for each model.
    shroom2.set_default_trajectory_frame(frame)
    rock1.set_default_trajectory_frame(frame)

    # Find the indices of the atoms that come in close
    # contact with atoms of the other model.
    shroom2_indx, rock1_indx = 
        shroom2.select_close_atoms_from_different_molecules(
            rock1, 3.0
        )

    # Update the counts
    shroom2_counts[shroom2_indx] += 1
    rock1_counts[rock1_indx] += 1

# Normalize the counts so the range extends from 0.0 to at
# most 1.0.
shroom2_counts = shroom2_counts / traj_length
rock1_counts = rock1_counts / traj_length 

# Replace the occupancies with these normalized count
# values.
shroom2_atom_info = shroom2.get_atom_information()
rock1_atom_info = rock1.get_atom_information()

shroom2_atom_info["occupancy"] = shroom2_counts
rock1_atom_info["occupancy"] = rock1_counts

shroom2.set_atom_information(shroom2_atom_info)
rock1.set_atom_information(rock1_atom_info)

# Save the first frame of each trajectory, with the updated
# occupancies.
print("Writing output files...")
shroom2.save_pdb("./shroom2_contacts.pdb", frame = 0)
rock1.save_pdb("./rock1_contacts.pdb", frame = 0)
