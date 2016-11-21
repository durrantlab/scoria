import pymolecule.dumbpy as numpy

print "make a1"
a1 = numpy.array([1,2,3])

print "make a2"
a2 = numpy.array([1,2,3])

print "make a3"
a3 = numpy.array([[1,2,3], [1,2,3]])

print "make a4"
a4 = numpy.array([[2,2,2], [2,2,2]])

numpy.vstack((a1, a2))

a5 = numpy.array([a1])
print "moo", a4 + a5

import pdb; pdb.set_trace()
