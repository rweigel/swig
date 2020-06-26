import numpy
import inplace_cpp
b = numpy.array([1,2,3], 'f')
inplace_cpp.inplacefn(b, len(b))
print(b)
