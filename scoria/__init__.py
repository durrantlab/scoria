# MIT License

# Copyright 2017 Jacob D. Durrant

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.


from __future__ import absolute_import
from scoria.Information import Information
from scoria.AtomsAndBonds import AtomsAndBonds
from scoria.FileIO import FileIO
from scoria.Geometry import Geometry
from scoria.Manipulation import Manipulation
from scoria.Molecule import Molecule
from scoria.OtherMolecules import OtherMolecules
from scoria.Quaternion import Quaternion
from scoria.Selections import Selections
from scoria.Test import Test

# By default, leave these commented out. They require numpy and so break pypy
# compatibility. Just uncomment when you want to test.
# from scoria.unittests.UnitTests import UnitTests

__version__ = "2.0"
