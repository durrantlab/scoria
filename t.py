#import numpy
from pymolecule import dumbpy as numpy

t = numpy.array([1,0,1])
print t
print t.shape
print numpy.nonzero(t)


#t = numpy.array([[0,0,1], [0,1,0], [1,0,0]])
#print numpy.nonzero(t)
#print  t
#print t.shape
