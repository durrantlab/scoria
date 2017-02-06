import numpy
import scoria

m1 = scoria.Molecule()
m2 = scoria.Molecule()

m1.load_pdb_into("test.pdb", False, False, False, False)
m2.load_pdb_into("test.pdb", False, False, False, False)

# move m2 so an alignment is needed.
m2.translate_molecule(numpy.array([15.0, 15.0, 15.0]))
m2.rotate_molecule_around_a_line_between_atoms(1, 25, 23.4)

# Now define the tethers.
CA1 = m1.select_atoms({"name": "CA"})
CA2 = m2.select_atoms({"name": "CA"})

tethers = zip(CA1, CA2)
m3 = m1.get_other_molecules_aligned_to_this(m2, tethers)

m1.save_pdb("aligned1.pdb")
m3.save_pdb("aligned2.pdb")

# aligned1.pdb and aligned2.pdb are right on top of each other.
