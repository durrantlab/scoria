import unittest
import os
import sys

import numpy as np
import scipy
import scoria


class OtherMoleculeTests(unittest.TestCase):
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
    def test_get_other_molecules_aligned_to_this(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_steric_clash_with_another_molecules(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_merge_with_another_molecules(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_get_distance_to_another_molecules(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_get_rmsd_equivalent_atoms_specified(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_get_rmsd_order_dependent(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_get_rmsd_heuristic(self):
        """
        Empty test.
        """
        pass
