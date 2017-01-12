import itertools as it
import pymolecule
import numpy as np
import Contact as con


# Defining the input files
PSF = "../pymolecule/sample_files/test_sim.psf"
DCD = "../pymolecule/sample_files/test_sim.dcd"

# Defining the two subsections to compare by a list of resid identifiers.
residA = range(1, 181)
residB = range(182, 297)

# Defining the output locations for the two subsections
Component_A_out = "./Component_A.pdb"
Component_B_out = "./Component_B.pdb"


# Load in a DCD/PSF trajectory and create a contact object within it.
print("Loading Molecule...             ",)
MOL = pymolecule.Molecule()
MOL.load_via_MDAnalysis(PSF, DCD)
contacts = con.Contact(MOL)
print(" done")


# Create the subsections based on the resid ranges defined previously
print("Creating Component Molecules... ",)
contacts.set_subsections(residA, residB)
print(" done")


# Calculate the contact points between the two subsections.
print("Calculating contacts...         ",)
contacts.calculate_contact()
print(" done")

#Save pdbs (with those occupancies) to two different files
print("Writing output files...         ",)
contacts.print_subcomponents("Part_A.pdb", "Part_B.pdb")
print(" done")
