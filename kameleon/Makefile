# Tested on Ubuntu 18.04

# To compile and run code, you need libcdf.so and libccmc.so.6.1.0.0
# See http://github.com/rweigel/kameleon for instructions on creating these libraries.
 
# Compare speed of interpolation between
# (1) Interpolating N points using a command line program
#     ./kameleon_cl FILENAME N
# (2) Doing the same with a call from Python
#     import _kameleon as kameleon
#     b = kameleon.runner(N)
# As expected, timing is similar.
#
# The next step is to write a program that allows
# (3) V_interpolated = kameleon.runner(X, Y, Z, V)
# instead of only
# (4) for i in range(X)
#       V_interpolated[i] = kameleon.runner(X[i], Y[i], Z[i], V[i])
# Method (3) is expected to be about 3x faster than (4), which is currently used.
# The 3x speed-up was determined by comparing the kameleon_cl code
# here doing the equivalent interpolation with the Kameleon/Python
# code as in
# https://github.com/GaryQ-physics/magnetosphere/blob/master/misc/kameleon_kamodo_compare/kameleon_version_testScript.py

# One way of doing this is with swig, but perhaps an easier way is with ctypes, e.g.,
# https://stackoverflow.com/questions/5862915/passing-numpy-arrays-to-a-c-function-for-input-and-output

# Edit these three paths
CDF_DIR=/home/osboxes/git/kameleon/deps/cdf36_4-dist
KAMELEON_PLUS=/home/osboxes/git/kameleon/ccmc-software/kameleon-plus/trunk/kameleon-plus-working
BOOST_ROOT=/home/osboxes/git/kameleon/deps/boost_1_67_0

CDF_LIB=${CDF_DIR}/src/lib
CDF_SO=$(CDF_LIB)/libcdf.so

KAMELEON_INCLUDE=$(KAMELEON_PLUS)/src
KAMELEON_LIB=$(KAMELEON_PLUS)/lib/ccmc
KAMELEON_SO=$(KAMELEON_LIB)/libccmc.so.6.1.0.0

TESTFILE=3d__var_3_e20031120-070000-000.out.cdf 1000000

SHELL := /bin/bash

all:
	make kameleon_so
	make kameleon_cl

test:
	make test_cl
	make test_so

kameleon_so:
	make _kameleon.so

_kameleon.so: kameleon_so.cpp $(KAMELEON) $(CDF)
	rm -f build/lib.linux-x86_64-2.7/_kameleon.so
	python setup.py build_ext --swig-opts=-c++ -lcdf -lccmc \
	-LCDF_LIB=${CDF_LIB} -L${KAMELEON_LIB} -I${KAMELEON_INCLUDE}:${BOOST_ROOT}
	cp build/lib.linux-x86_64-2.7/_kameleon.so .

test_so:
	make testfile
	LD_LIBRARY_PATH=${CDF_LIB}:${KAMELEON_LIB} python kameleon_test.py 

kameleon_cl: kameleon_cl.cpp $(KAMELEON_INCLUDE) $(BOOST_ROOT)
	g++ kameleon_cl.cpp -Wno-deprecated -o kameleon_cl \
		-I${BOOST_ROOT} -I${KAMELEON_INCLUDE} \
		-L$(KAMELEON_LIB) \
		-lccmc \
		-lboost_system -lboost_python -lpython2.7 -I/usr/include/python2.7
# Last line above needed for Boost's wrap_python.hpp (based on error message without it)

test_cl: kameleon_cl
	make testfile
	LD_LIBRARY_PATH=$(KAMELEON_LIB) ./kameleon_cl $(TESTFILE) 1000000

testfile:
	- wget -q -N http://mag.gmu.edu/git-data/sblake/SCARR5_GM_IO2/IO2/$(TESTFILE)

clean:
	- rm *.cdf
	- rm kameleon_cl
	- rm _kameleon.so
	- rm -f *~

distclean:
	make clean
	rm -rf build
	- rm -f kameleon_cl 3d__var_3_e20031120-070000-000.out.cdf	
