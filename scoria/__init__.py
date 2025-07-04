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
from scoria.unittests.UnitTests import UnitTests

__version__ = "1.0.6"
