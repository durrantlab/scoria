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
        if not os.path.exists("./scoria_tests_tmp"):
            os.mkdir("./scoria_tests_tmp")

        self.mol = scoria.Molecule()

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

    @unittest.skip("Needs test written")
    def test_set_atom_location(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_translate_molecule(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_rotate_molecule_around_a_line_between_points(self):
        """
        Empty test.
        """
        pass

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
        pass

    @unittest.skip("Needs test written")
    def test_rotate_molecule_around_pivot_atom(self):
        """
        Empty test.
        """
        pass
