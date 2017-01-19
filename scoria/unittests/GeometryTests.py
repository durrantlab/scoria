import unittest
import os
import sys

import numpy as np
import scipy
import scoria


class GeometryTests(unittest.TestCase):
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
    def test_get_angle_between_three_points(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_get_dihedral_angle(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_is_planar(self):
        """
        Empty test.
        """
        pass

    @unittest.skip("Needs test written")
    def test_get_planarity_deviation(self):
        """
        Empty test.
        """
        pass
