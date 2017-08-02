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
import scoria.six as six
#from .six import string_types as six_string_types


def var_type(var):
    """A helper function to identify a variable's type.

        Args:
            var  -- The variable.

        Returns:
            A string, the variable type.
    """

    if isinstance(var, six.string_types):
        return "string"
    
    # See if it's one of your dumbpy array objects
    try: return var.type
    except: pass

    # see if it's a list
    if type(var) is list:
        return "list"
    else:
        # a number perhaps?
        return "number"

def to_list(arr):
    """Convert an array to a list.

        Args:
            arr  -- A 1D or 2D array.

        Returns:
            The list.
    """

    # return a list regardless of whether arr is a list or array.
    typ = var_type(arr) 
    if typ in ["1D", "2D"]:
        return arr.lst[:]
    elif typ == "list":
        # already a python list
        return arr[:]
    else:
        # a number or string
        return arr
