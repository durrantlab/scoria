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
        info_path = os.path.dirname(os.path.abspath(__file__)) + '/../sample_files/'
        self.mol = scoria.Molecule(info_path + '3_mol_test.pdb')
        self.other_mol = scoria.Molecule(info_path + 'other_mol_test.pdb')

    def tearDown(self):
        """
        Cleans up variables for the next test.
        """
        self.mol = None

    ### Tests

    def test_select_atoms(self):
        """
        Empty test.
        """

        # Testing empty criteria
        selection_criteria = {}
        expected_selection = range(0, 12)
        selection = list(self.mol.select_atoms(selection_criteria))

        self.assertEqual(selection, expected_selection)

        # Testing improper criteria
        selection_criteria = {'name':['xxx']}
        expected_selection = []
        selection = list(self.mol.select_atoms(selection_criteria))

        self.assertEqual(selection, expected_selection)


        # Testing name
        selection_criteria = {'name':['N']}
        expected_selection = [2]
        selection = list(self.mol.select_atoms(selection_criteria))

        self.assertEqual(selection, expected_selection)

        selection_criteria = {'name':['N', 'N1']}
        expected_selection = [0, 2]
        selection = list(self.mol.select_atoms(selection_criteria))

        self.assertEqual(selection, expected_selection)

        # Testing element
        selection_criteria = {'element':['N']}
        expected_selection = [0, 2, 8, 11]
        selection = list(self.mol.select_atoms(selection_criteria))

        self.assertEqual(selection, expected_selection)

        selection_criteria = {'element':['N', 'O']}
        expected_selection = [0, 2, 5, 8, 11]
        selection = list(self.mol.select_atoms(selection_criteria))

        self.assertEqual(selection, expected_selection)

        # Testing resname
        selection_criteria = {'resname':['HIS']}
        expected_selection = range(2, 12)
        selection = list(self.mol.select_atoms(selection_criteria))

        self.assertEqual(selection, expected_selection)

        selection_criteria = {'resname':['U']}
        expected_selection = [0]
        selection = list(self.mol.select_atoms(selection_criteria))

        self.assertEqual(selection, expected_selection)


    def test_select_atoms_in_bounding_box(self):
        """
        Empty test.
        """
        bound_all = self.mol.get_bounding_box(padding=0.5)
        expected_selection = range(0, 12)
        selection = list(self.mol.select_atoms_in_bounding_box(bound_all))

        self.assertEqual(selection, expected_selection)


        bound_all = self.mol.get_bounding_box()
        expected_selection = range(0, 12)
        selection = list(self.mol.select_atoms_in_bounding_box(bound_all))

        self.assertEqual(selection, expected_selection)



    def test_select_all_atoms_bound_to_selection(self):
        """
        Empty test.
        """
        prior_selection = [0]
        expected_selection = []
        selection = list(self.mol.select_all_atoms_bound_to_selection(prior_selection))

        self.assertEqual(selection, expected_selection)

        prior_selection = [2]
        expected_selection = [3]
        selection = list(self.mol.select_all_atoms_bound_to_selection(prior_selection))

        self.assertEqual(selection, expected_selection)

        prior_selection = [3]
        expected_selection = [2, 4, 6]
        selection = list(self.mol.select_all_atoms_bound_to_selection(prior_selection))

        self.assertEqual(selection, expected_selection)


    def test_select_branch(self):
        """
        Empty test.
        """
        expected_selection = range(2, 12)
        selection = list(self.mol.select_branch(2, 3))
        selection.sort() # The branch is not in indexed order

        self.assertEqual(selection, expected_selection)


    def test_select_atoms_from_same_molecule(self):
        """
        Empty test.
        """
        prior_selection = [0]
        expected_selection = [0]
        selection = list(self.mol.select_atoms_from_same_molecule(prior_selection))

        self.assertEqual(selection, expected_selection)

        prior_selection = [2]
        expected_selection = range(2, 12)
        selection = list(self.mol.select_atoms_from_same_molecule(prior_selection))

        self.assertEqual(selection, expected_selection)

    def test_selections_of_constituent_molecules(self):
        """
        Empty test.
        """
        molecules = self.mol.selections_of_constituent_molecules()
        expected_molecules = [[0], [1], range(2, 12)]

        for i in [0, 1, 2]:
            self.assertEqual(list(molecules[i]), expected_molecules[i])


    def test_select_atoms_near_other_selection(self):
        """
        Empty test.
        """
        source_selection = [2]
        expected_selection = [3]
        selection = self.mol.select_atoms_near_other_selection(source_selection, 2.0)

        self.assertEqual(list(selection), expected_selection)


    def test_select_atoms_in_same_residue(self):
        """
        Empty test.
        """
        source_selection = [0]
        expected_selection = [0]
        selection = self.mol.select_atoms_in_same_residue(source_selection)

        self.assertEqual(list(selection), expected_selection)

        source_selection = [2]
        expected_selection = range(2, 12)
        selection = self.mol.select_atoms_in_same_residue(source_selection)

        self.assertEqual(list(selection), expected_selection)


    def test_invert_selection(self):
        """
        Empty test.
        """
        source_selection = [0]
        expected_selection = range(1, 12)
        selection = self.mol.invert_selection(source_selection)

        self.assertEqual(list(selection), expected_selection)

        source_selection = [11]
        expected_selection = range(0, 11)
        selection = self.mol.invert_selection(source_selection)

        self.assertEqual(list(selection), expected_selection)

        source_selection = [5]
        expected_selection = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
        selection = self.mol.invert_selection(source_selection)

        self.assertEqual(list(selection), expected_selection)


    def test_select_all(self):
        """
        Empty test.
        """
        expected_selection = range(0, 12)
        selection = self.mol.select_all()

        self.assertEqual(list(selection), expected_selection)


    def test_select_close_atoms_from_different_molecules(self):
        """
        Empty test.
        """
        expected_selection = range(0, 12)
        selection = self.mol.select_close_atoms_from_different_molecules(self.mol, 0.1)

        self.assertEqual(list(selection[0]), expected_selection)

        expected_selection = []
        selection = self.mol.select_close_atoms_from_different_molecules(self.other_mol, 0.1)

        self.assertEqual(list(selection[0]), expected_selection)


    def test_get_molecule_from_selection(self):
        """
        Empty test.
        """
        desired_selection = [1]
        new_mol = self.mol.get_molecule_from_selection(desired_selection)

        old_coordinates = self.mol.get_coordinates()
        new_coordinates = new_mol.get_coordinates()

        self.assertEqual(len(new_coordinates), 1)
        self.assertEqual(list(new_coordinates[0]), list(old_coordinates[1]))


    def test_selections_of_chains(self):
        """
        Empty test.
        """
        chain_selections = self.mol.selections_of_chains()

        self.assertEqual(len(chain_selections), 2)
        self.assertEqual(list(chain_selections['B']), [0, 1])
        self.assertEqual(list(chain_selections['A']), range(2, 12))

    def test_selections_of_residues(self):
        """
        Empty test.
        """
        residue_selections = self.mol.selections_of_residues()

        self.assertEqual(list(residue_selections['HIS-985-A']), range(2, 12))
        self.assertEqual(list(residue_selections['U-71-B']), [0])
        self.assertEqual(list(residue_selections['DT-13-B']), [1])