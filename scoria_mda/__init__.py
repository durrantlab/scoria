# Scoria MDA is a program for manipulating 3D molecular models
# that includes MDAnalysis support.
# 
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
from scoria_mda.Information import Information
from scoria_mda.AtomsAndBonds import AtomsAndBonds
from scoria_mda.FileIO import FileIO
from scoria_mda.Geometry import Geometry
from scoria_mda.Manipulation import Manipulation
from scoria_mda.Molecule import Molecule
from scoria_mda.OtherMolecules import OtherMolecules
from scoria_mda.Quaternion import Quaternion
from scoria_mda.Selections import Selections
# from scoria_mda.Test import Test

# By default, leave these commented out. They require numpy and so break pypy
# compatibility. Just uncomment when you want to test.
# from scoria_mda.unittests.UnitTests import UnitTests

__version__ = "2.0"
