import numpy
import inplace
b = numpy.array([1,2,3],'d')
inplace.inplace(b)
print(b)