# Scoria is a program for manipulating 3D molecular models.
# Copyright (C) 2017  Jacob D. Durrant
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Note that this version of Scoria (with MDAnalysis integration) is
# derived from the original Scoria source code, which retains its
# Apache 2.0 license.

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
# from scoria.Test import Test

# By default, leave these commented out. They require numpy and so break pypy
# compatibility. Just uncomment when you want to test.
# from scoria.unittests.UnitTests import UnitTests

__version__ = "2.0"
