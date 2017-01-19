import unittest
import os
import sys

import numpy as np
import scipy
import scoria


class SelectionsTests(unittest.TestCase):
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
    def test_select_atoms(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_select_atoms_in_bounding_box(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_select_all_atoms_bound_to_selection(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_select_branch(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_select_atoms_from_same_molecule(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_selections_of_constituent_molecules(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_select_atoms_near_other_selection(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_select_atoms_in_same_residue(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_invert_selection(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_select_all(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_select_close_atoms_from_different_molecules(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_get_molecule_from_selection(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_selections_of_chains(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_selections_of_residues(self):
        """
        Empty test.
        """
        pass
