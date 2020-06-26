from distutils.core import *
from distutils      import sysconfig

_kameleon = Extension("_kameleon", ["kameleon.i","kameleon_so.cpp"])

setup(  name        = "",
        description = "",
        author      = "R.S. Weigel",
        version     = "0.0.1",
        ext_modules = [_kameleon]
        )
