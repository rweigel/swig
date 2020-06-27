import numpy
import ctypes

indata = numpy.ones((5,6), dtype=numpy.double)
outdata = numpy.zeros((5,6), dtype=numpy.double)
lib = ctypes.cdll.LoadLibrary('./simple.so')
fun = lib.cfun

fun(ctypes.c_void_p(indata.ctypes.data), 
	ctypes.c_int(5), 
	ctypes.c_int(6),
    ctypes.c_void_p(outdata.ctypes.data))
print 'indata: %s' % indata
print 'outdata: %s' % outdata