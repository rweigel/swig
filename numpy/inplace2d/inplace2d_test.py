import numpy
import inplace2d
a = numpy.array([[1,2,3],[3,4,5]], 'd')
inplace2d.inplace2d(a)
print(a)