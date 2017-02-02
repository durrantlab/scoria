import unittest
import os
import sys

import numpy as np
import scipy
import scoria


class ManipulationTests(unittest.TestCase):
    """
    Base Test Suite
    """

    # Initialization and destruction for each test.

    def setUp(self):
        """
        Setting up the test molecule.
        """
        info_path = os.path.dirname(os.path.abspath(__file__)) + '/../sample_files/'
        self.mol = scoria.Molecule(info_path + '3_mol_test.pdb')

        self.accuracy = 4

    def tearDown(self):
        """
        Cleans up variables for the next test.
        """
        self.mol = None

        # Remove all files from the tmp folder?

    ### Tests

    @unittest.skip("Needs test written")
    def test_set_coordinate_undo_point(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_coordinate_undo(self):
        """
        Empty test.
        """
        pass

    def test_set_atom_location(self):
        """
        Empty test.
        """
        original = self.mol.get_coordinates()[1]
        delta = self.mol.set_atom_location(0, np.array([20.0, 20.0, 20.0]))

        self.assertEqual(len(delta), 3)

        distance = (original + delta)
        moved = self.mol.get_coordinates()[1]

        self.assertEqual(list(distance), list(moved))

    def test_translate_molecule(self):
        """
        Empty test.
        """
        original = self.mol.get_coordinates()[0]
        delta = np.array([10.0, 10.0, 10.0])

        self.mol.translate_molecule(delta)

        moved = self.mol.get_coordinates()[0]
        distance = original + delta

        self.assertEqual(list(moved), list(distance))

    def test_rotate_molecule_around_a_line_between_points(self):
        """
        Empty test.
        """ 
        one = np.array([0.0, 0.0, 0.0])
        two = np.array([1.0, 0.0, 0.0])
        radians = np.radians(180.0)

        original = self.mol.get_coordinates()[0]

        self.mol.rotate_molecule_around_a_line_between_points(one, two, radians)

        new = self.mol.get_coordinates()[0]
        expected = [10.0, -10.0, -10.0]
        for i in range(0,3):
            self.assertAlmostEqual(list(new)[i], expected[i], self.accuracy)

    @unittest.skip("Needs test written")
    def test_rotate_molecule_around_a_line_between_atoms(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_rotate_molecule_around_pivot_point(self):
        """
        Empty test.
        """
        self.mol.rotate_molecule_around_pivot_point([0,0,0], 0.0, 180.0, 180.0)

    @unittest.skip("Needs test written")
    def test_rotate_molecule_around_pivot_atom(self):
        """
        Empty test.
        """
        pass
