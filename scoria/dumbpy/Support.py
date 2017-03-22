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
