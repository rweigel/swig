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
_inplace_cpp = Extension("_inplace_cpp",
                   ["inplace_cpp.i","inplace.cpp"],
                   include_dirs = [numpy_include],
                   )

# NumyTypemapTests setup
setup(  name        = "",
        description = "",
        author      = "",
        version     = "",
        ext_modules = [_inplace_cpp]
        )
