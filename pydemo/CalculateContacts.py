import itertools as it
import pymolecule
import numpy as np
import Contact as con


counts = [{},{}]

PSF = "/home/pjropp/Source/pymolecule2/pymolecule/sample_files/test_sim.psf"
DCD = "/home/pjropp/Source/pymolecule2/pymolecule/sample_files/test_sim.dcd"


print "Loading Molecule...",
# Load in a DCD/PSF trajectory.
MOL = pymolecule.Molecule()
MOL.load_via_MDAnalysis(PSF, DCD)

contacts = con.Contact(MOL)
print " done"

print "Creating Component Molecules...",
# Create the serial ranges
serialA = range(1, 181)
serialB = range(182, 297)

contacts.set_subsections(serialA, serialB)
print " done"

print "Calculating contacts...",

contacts.calculate_contact()

print " done"

#Save pdbs (with those occupancies) to two different files
moleculeA.save_pdb("Part_A.pdb",False)
moleculeB.save_pdb("Part_B.pdb",False)

