# Overview

A Python wrapper to the C++ Kameleon interpolation library.

The (Kameleon Plus)[https://ccmc.gsfc.nasa.gov/Kameleon] includes a Python wrapper that allows one to call its C++ interpolation function with only one point. The code here allows one to call the Kameleon C++ interpolation function with an array of points. The typical speed-up is 3x over looping in Python over an array of points.

The Kamodo library also includes a Python wrapper to the Kameleon C++ interpolation library. Interpolation over an array of points is typically 30x slower than that from using this library.

[Test script](https://github.com/GaryQ-physics/magnetosphere/blob/master/misc/kameleon_kamodo_compare/kameleon_version_testScript.py) comparing interpolation speed between the Kamelon and Kamodo Python wrappers.

# Installation and Use

Download and unzip kameleonA.zip

Download a test file to `/tmp`

```
sys.path.append('/path/of/kameleonA')
import _kameleon as kameleon
x = [1., 2.]
y = [1., 2.]
z = [1., 2.]
x = kameleonA.interpolate('/tmp/3d__var_3_e20031120-070000-000.out.cdf', x, y, z, len(x))
print(x)
```

# Compiling

## Step 1
```
git clone https://github.com/rweigel/kameleon
```
Then read `README.md` for instructions

## Step 2

```
git clone https://github.com/rweigel/swig-and-ctypes
cd swig-and-ctypes
# Edit paths in Makefile
make test_so
```

# Notes

Here SWIG was used, but perhaps this is easier donw with ctypes, e.g., https://stackoverflow.com/questions/5862915/passing-numpy-arrays-to-a-c-function-for-input-and-output

See end of the Makefile for description of why using the libraries from https://ccmc.gsfc.nasa.gov/Kameleon/Quick_start.html does not work.

