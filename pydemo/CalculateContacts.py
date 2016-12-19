import itertools as it
import pymolecule
import numpy as np
import Contact as con


# Defining the input files
PSF = "/home/pjropp/Source/pymolecule2/pymolecule/sample_files/test_sim.psf"
DCD = "/home/pjropp/Source/pymolecule2/pymolecule/sample_files/test_sim.dcd"

# Defining the two subsections to compare by a list of serial identifiers.
serialA = range(1, 181)
serialB = range(182, 297)

# Defining the output locations for the two subsections
Component_A_out = "/home/pjropp/Source/pymolecule2/pymolecule/pydemo/Component_A.pdb"
Component_B_out = "/home/pjropp/Source/pymolecule2/pymolecule/pydemo/Component_B.pdb"


# Load in a DCD/PSF trajectory and create a contact object within it.
print "Loading Molecule...             ",
MOL = pymolecule.Molecule()
MOL.load_via_MDAnalysis(PSF, DCD)

contacts = con.Contact(MOL)
print " done"


# Create the subsections based on the serial ranges defined previously
print "Creating Component Molecules... ",
contacts.set_subsections(serialA, serialB)

print " done"


# Calculate the contact points between the two subsections.
print "Calculating contacts...         ",
contacts.calculate_contact()

print " done"

#Save pdbs (with those occupancies) to two different files
print "Writing output files...         ",
contacts.print_subcomponents("Part_A.pdb", "Part_B.pdb")

print " done"
