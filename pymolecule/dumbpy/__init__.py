# A numpy replacement. Basically numpy, with non-numpy as a backup.
try:
    # Try to load traditional numpy
    #sdf
    from numpy import array
    from numpy.core.defchararray import strip as defchararray_strip 
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
except:
    # Numpy not available, so load substitute
    from Array import array
    from Utils import genfromtxt
    from Utils import nonzero
    from Utils import logical_or
    from Utils import defchararray_strip

try:
    # Try to load traditional scipy
    sdf
    from scipy.spatial.distance import squareform
    from scipy.spatial.distance import pdist
    from scipy.spatial.distance import cdist
except:
    # Use cheap replacement instead.
    pass