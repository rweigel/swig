import numpy
import inplace_cpp
b = numpy.array([1,2,3], 'd')
inplace_cpp.inplacefn(b)
assert(numpy.all(b == [2., 4., 6.]))
print('PASS')
