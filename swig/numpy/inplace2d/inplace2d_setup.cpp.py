# System imports
from distutils.core import *
from distutils      import sysconfig

# Third-party modules - we depend on numpy for everything
import numpy

# Obtain the numpy include directory.  This logic works across numpy versions.
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

print(numpy_include)
# inplace extension module
_inplace2d = Extension("_inplace2d",
                   ["inplace2d.i","inplace2d.cpp"],
                   include_dirs = [numpy_include],
                   )

# NumyTypemapTests setup
setup(  name        = "inplace function",
        description = "inplace takes a double array and doubles each of its elements in-place.",
        author      = "Egor Zindy",
        version     = "1.0",
        ext_modules = [_inplace2d]
        )
