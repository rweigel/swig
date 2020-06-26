# System imports
from distutils.core import *
from distutils      import sysconfig
_code = Extension("_code",
                   ["code.i","code.cpp"])

# ezrange setup
setup(  name        = "",
        description = "",
        author      = "",
        version     = "0.0.1",
        ext_modules = [_code]
        )
