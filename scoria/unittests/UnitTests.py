import unittest
import InformationTests as IT
import FileIOTests as FIOT
import GeometryTests as GT
import ManipulationTests as MT
import OtherMoleculeTests as OMT
import SelectionTests as ST

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class UnitTests():
    """
    Unit testing object for scoria.
    """
    def __init__(self):
        """
        Initalizes the unit tests.
        """
        self._suite = unittest.TestSuite()
        self._runner = unittest.TextTestRunner()

    def add_all_tests(self):
        """
        Adds all available tests to the suite.
        """
        self.add_information_tests()
        self.add_fileio_tests()
        self.add_geometry_tests()
        self.add_selection_tests()
        self.add_manipulation_tests()
        self.add_other_molecule_tests()

    def run(self):
        """
        Runs the currently queued suite of tests.
        """
        self._runner.run(self._suite)

    def run_all(self):
        """
        Quickly runs all unit tests.
        """
        self.add_all_tests()
        self.run()

    def add_information_tests(self):
        """
        Adds the information tests.
        """
        information_tests = unittest.makeSuite(IT.InformationTests)
        self._suite.addTests(information_tests)

    def add_fileio_tests(self):
        """
        Adds the information tests.
        """
        fileio_tests = unittest.makeSuite(FIOT.FileIOTests)
        self._suite.addTests(fileio_tests)

    def add_geometry_tests(self):
        """
        Adds the information tests.
        """
        tests = unittest.makeSuite(GT.GeometryTests)
        self._suite.addTests(tests)
        

    def add_manipulation_tests(self):
        """
        Adds the information tests.
        """
        tests = unittest.makeSuite(MT.ManipulationTests)
        self._suite.addTests(tests)

    def add_other_molecule_tests(self):
        """
        Adds the information tests.
        """
        tests = unittest.makeSuite(OMT.OtherMoleculeTests)
        self._suite.addTests(tests)

    def add_selection_tests(self):
        """
        Adds the information tests.
        """
        tests = unittest.makeSuite(ST.SelectionsTests)
        self._suite.addTests(tests)
        
        