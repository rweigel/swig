import numpy
import inplace_c
b = numpy.array([1,2,3],'d')
inplace_c.inplacefn(b)
assert(numpy.all(b == [2., 4., 6.]))
print('PASS')
