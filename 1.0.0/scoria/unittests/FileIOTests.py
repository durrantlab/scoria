# Copyright 2017 Jacob D. Durrant
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
import unittest
import os
import sys
import shutil

#import numpy as np
from scoria import dumbpy as np

# No MDAnalysis in Apache 2.0 version! #try: import MDAnalysis  # pypy shouldn't be able to load this.
# No MDAnalysis in Apache 2.0 version! #except: pass

import scoria
import shutil


class FileIOTests(unittest.TestCase):
    """
    Base Test Suite
    """

    # Initialization and destruction for each test.

    def setUp(self):
        """
        Setting up the test molecule.
        """
        self.info_path = os.path.dirname(os.path.abspath(__file__)) + '/../sample-files/'
        self.mol = scoria.Molecule()

        self.output_name = None

    def tearDown(self):
        """
        Cleans up variables for the next test.
        """
        self.mol = None

        if self.output_name is not None:
            if os.path.isdir(self.output_name):
                shutil.rmtree(self.output_name)
            elif os.path.isfile(self.output_name):
                os.remove(self.output_name)

    ### Tests
    # Loaders

    @unittest.skip("Need to implement")
    def test_init_file_loader(self):
        """
        
        """
        pass

    def test_load_pym_into(self):
        """
        Testing the ability of the FileIO module to import pym files.
        """
        self.mol.load_pym_into(self.info_path + 'file_io_test.pym')

        self.assertEqual(self.mol.get_total_number_of_atoms(), 401)
        self.assertEqual(self.mol.get_remarks(), [' This is a remark.'])

    @unittest.skip("Needs multiframe pdbqt")
    def test_load_pdbqt_trajectory_into(self):
        """
        Testing the ability of the FileIO module to import pdbqt trajectories
        from a file name.
        """
        self.mol.load_pdbqt_trajectory_into(self.info_path + '')

    @unittest.skip("Needs multiframe pdbqt")
    def test_load_pdbqt_trajectory_into_using_file_object(self):
        """
        Testing the ability of the FileIO module to import pdbqt trajectories
        from a file object.
        """
        with open(self.info_path + 'test_trajectory.pdbqt') as pdbqt_file:
            self.mol.load_pdb_trajectory_into_using_file_object(pdbqt_file)

            # Assert that the molecules are correct
            # Assert the trajectory is the correct length

    def test_load_pdbqt_into(self):
        """
        Testing the ability of the FileIO module to import pdbqt from a
        file name.
        """
        pdbqt_file_name = self.info_path + 'single_frame.pdbqt'
        self.mol.load_pdbqt_into(pdbqt_file_name)

        self.assertEqual(self.mol.get_total_number_of_atoms(), 489)
        self.assertEqual(self.mol.get_remarks(), [])
        self.assertEqual(self.mol.get_trajectory_frame_count(), 1)

        # Perhaps make more specialized remarks?

    def test_load_pdbqt_into_using_file_object(self):
        """
        Empty test.
        """
        pdbqt_file_name = self.info_path + 'single_frame.pdbqt'
        with open(pdbqt_file_name) as pdbqt_file:
            self.mol.load_pdbqt_into_using_file_object(pdbqt_file)

            self.assertEqual(self.mol.get_total_number_of_atoms(), 489)
            self.assertEqual(self.mol.get_remarks(), [])
            self.assertEqual(self.mol.get_trajectory_frame_count(), 1)

    @unittest.skip("Needs pdb trajectory file")
    def test_load_pdb_trajectory_into(self):
        """
        Empty test.
        """
        pdb_file_name = self.info_path + 'trajectory.pdb'
        self.mol.load_pdbqt_into(pdb_file_name)

        self.assertEqual(self.mol.get_total_number_of_atoms(), 0)
        self.assertEqual(self.mol.get_remarks(), [])
        self.assertEqual(self.mol.get_trajectory_frame_count(), 0)

    @unittest.skip("Needs pdb trajectory file")
    def test_load_pdb_trajectory_into_using_file_object(self):
        """
        Empty test.
        """
        pdb_file_name = self.info_path + 'trajectory.pdb'
        with open(pdb_file_name) as pdb_file:
            self.mol.load_pdbqt_into_using_file_object(pdb_file)

            self.assertEqual(self.mol.get_total_number_of_atoms(), 489)
            self.assertEqual(self.mol.get_remarks(), [])
            self.assertEqual(self.mol.get_trajectory_frame_count(), 0)

    def test_load_pdb_into(self):
        """
        Empty test.
        """
        pdb_file_name = self.info_path + 'single_frame.pdb'
        self.mol.load_pdbqt_into(pdb_file_name)

        self.assertEqual(self.mol.get_total_number_of_atoms(), 401)
        self.assertEqual(self.mol.get_remarks(), [" This is a remark."])

    def test_load_pdb_into_using_file_object(self):
        """
        Empty test.
        """
        pdb_file_name = self.info_path + 'single_frame.pdb'
        with open(pdb_file_name) as pdb_file:
            self.mol.load_pdbqt_into_using_file_object(pdb_file)

            self.assertEqual(self.mol.get_total_number_of_atoms(), 401)
            self.assertEqual(self.mol.get_remarks(), [" This is a remark."])

    # No MDAnalysis in Apache 2.0 version! #def test_load_MDAnalysis_into(self):
    # No MDAnalysis in Apache 2.0 version! #    """
    # No MDAnalysis in Apache 2.0 version! #    Empty test.
    # No MDAnalysis in Apache 2.0 version! #    """
    # No MDAnalysis in Apache 2.0 version! #    test_dcd = self.info_path + 'single_frame.dcd'
    # No MDAnalysis in Apache 2.0 version! #    test_psf = self.info_path + 'single_frame.psf'
    # No MDAnalysis in Apache 2.0 version! #
    # No MDAnalysis in Apache 2.0 version! #    self.mol.load_MDAnalysis_into(test_psf, test_dcd)
    # No MDAnalysis in Apache 2.0 version! #
    # No MDAnalysis in Apache 2.0 version! #    self.assertEqual(self.mol.get_total_number_of_atoms(), 401)
    # No MDAnalysis in Apache 2.0 version! #    self.assertEqual(self.mol.get_remarks()[0:2],
    # No MDAnalysis in Apache 2.0 version! #                     ['     Created by DCD plugin\x00',
    # No MDAnalysis in Apache 2.0 version! #                      '     \x00\x00\x00REMARKS Created 03 January, 2017 at'])
    # No MDAnalysis in Apache 2.0 version! #
    # No MDAnalysis in Apache 2.0 version! #def test_load_MDAnalysis_into_using_universe_object(self):
    # No MDAnalysis in Apache 2.0 version! #    """
    # No MDAnalysis in Apache 2.0 version! #    Empty test.
    # No MDAnalysis in Apache 2.0 version! #    """
    # No MDAnalysis in Apache 2.0 version! #    test_dcd = self.info_path + 'single_frame.dcd'
    # No MDAnalysis in Apache 2.0 version! #    test_psf = self.info_path + 'single_frame.psf'
    # No MDAnalysis in Apache 2.0 version! #
    # No MDAnalysis in Apache 2.0 version! #    universe = MDAnalysis.Universe(test_psf, test_dcd)
    # No MDAnalysis in Apache 2.0 version! #
    # No MDAnalysis in Apache 2.0 version! #    self.mol.load_MDAnalysis_into_using_universe_object(universe)
    # No MDAnalysis in Apache 2.0 version! #
    # No MDAnalysis in Apache 2.0 version! #    self.assertEqual(self.mol.get_total_number_of_atoms(), 401)
    # No MDAnalysis in Apache 2.0 version! #    self.assertEqual(self.mol.get_remarks()[0:2],
    # No MDAnalysis in Apache 2.0 version! #                     ['     Created by DCD plugin\x00',
    # No MDAnalysis in Apache 2.0 version! #                      '     \x00\x00\x00REMARKS Created 03 January, 2017 at'])

    # Test Save functions

    def test_save_pym(self):
        """
        Empty test.
        """
        input_name = self.info_path + 'single_frame.pdb'
        self.output_name = 'output.pym'

        self.mol.load_pdb_into(input_name)
        self.mol.save_pym(self.output_name)

        self.assertTrue(os.path.exists(self.output_name))

    def test_save_pdb(self):
        """
        Empty test.
        """

        # Don't use pym file here. It's not compatible with pypy.
        #input_name = self.info_path + 'file_io_test.pym'
        #self.mol.load_pym_into(input_name)

        input_name = self.info_path + 'single_frame.pdb'
        self.output_name = 'output.pdb'

        self.mol.load_pdb_into(input_name)
        self.mol.save_pdb(self.output_name)

        self.assertTrue(os.path.exists(self.output_name))

