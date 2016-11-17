# A numpy replacement. Basically numpy, with non-numpy as a backup.
dependencies_available = []

force_dumbpy = True
try:
    # Try to load traditional numpy
    if force_dumbpy: raise ValueError('Using dumbpy')

    from numpy import array
    from numpy.core.defchararray import strip as defchararray_strip 
    from numpy.core.defchararray import add as defchararray_add
    from numpy.core.defchararray import rjust as defchararray_rjust
    from numpy.core.defchararray import upper as defchararray_upper
    from numpy.core.defchararray import lstrip as defchararray_lstrip
    from numpy.core.defchararray import split as defchararray_split
    from numpy.lib.recfunctions import append_fields
    from numpy import genfromtxt
    from numpy import nonzero
    from numpy import logical_or
    from numpy import core
    from numpy import dtype
    from numpy import vstack
    from numpy import zeros
    from numpy import max
    from numpy import unique
    from numpy import insert
    from numpy import logical_not
    from numpy import append
    from numpy import arange
    from numpy import savez
    from numpy import load
    from numpy import ones
    from numpy import logical_and
    from numpy import empty
    from numpy import sum
    from numpy import min
    from numpy import delete
    from numpy import setdiff1d
    from numpy import hstack
    from numpy import intersect1d
    from numpy import setxor1d
    from numpy import power
    from numpy import cos
    from numpy import sin
    from numpy import sqrt
    from numpy import dot
    from numpy import linalg
    from numpy import amin
    from numpy import lib
    from numpy import identity
    from numpy import mean
    from numpy import transpose
    from numpy import argmax
    from numpy import ma
    from numpy import arccos
    from numpy import cross
    from numpy import arctan2
    from numpy import fabs
    from numpy import ones
    from numpy import empty

    def get_col(arr, num):
        return arr[:, num]

    dependencies_available.append("NUMPY")
except:
    # Numpy not available, so load substitute
    from Array import array
    from Utils import genfromtxt
    from Utils import nonzero
    from Utils import logical_or
    from Utils import defchararray_strip
    from Utils import defchararray_add
    from Utils import defchararray_rjust
    from Utils import defchararray_upper
    from Utils import defchararray_lstrip
    from Utils import defchararray_split
    from DType import dtype
    from Utils import vstack
    from Utils import append_fields
    from Utils import zeros
    from Utils import max
    from Utils import unique
    from Utils import insert
    from Utils import logical_not
    from Utils import append
    from Utils import arange
    from Utils import get_col
    from Utils import ones
    from Utils import empty
    dependencies_available.append("DUMBPY")

try:
    # Try to load traditional scipy
    if force_dumbpy: raise ValueError('Using dumbpy')

    from scipy.spatial.distance import squareform
    from scipy.spatial.distance import pdist
    from scipy.spatial.distance import cdist
    dependencies_available.append("SCIPY")
except:
    # Use cheap replacement instead.
    pass

def class_dependency(action, dependency):
    global dependencies_available
    if not dependency in dependencies_available:
        print "Error: Cannot " + action + ". Install this recommended dependency: " + dependency
        return False
    return True
