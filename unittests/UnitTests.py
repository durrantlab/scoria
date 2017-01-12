import unittest

import InformationTests as IT

SUITE = unittest.TestSuite()
SUITE.addTests(unittest.makeSuite(IT.InformationTests))

RUN = unittest.TextTestRunner()
RUN.run(SUITE)
