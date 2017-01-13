import unittest
import InformationTests as IT

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
        information_tests = unittest.makeSuite(IT.InformationTests)
        self._suite.addTests(information_tests)

    def run_suite(self):
        """
        Runs the currently queued suite of tests.
        """
        self._runner.run(self._suite)

    def run_all_tests(self):
        """
        Quickly runs all unit tests.
        """
        self.add_all_tests()
        self.run_suite()
