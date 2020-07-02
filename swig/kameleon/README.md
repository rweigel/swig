# Overview

A Python wrapper to the C++ Kameleon interpolation library.

The (Kameleon Plus)[https://ccmc.gsfc.nasa.gov/Kameleon] includes a Python wrapper that allows one to call its C++ interpolation function with only one point. The code here allows one to call the Kameleon C++ interpolation function with an array of points. The typical speed-up is 3x over looping in Python over an array of points.

The Kamodo library also includes a Python wrapper to the Kameleon C++ interpolation library. Interpolation over an array of points is typically 30x slower than that from using this library.

[Test script](https://github.com/GaryQ-physics/magnetosphere/blob/master/misc/kameleon_kamodo_compare/kameleon_version_testScript.py) comparing interpolation speed between the Kamelon and Kamodo Python wrappers.

# Installation and Use

Tested on Python 2.7, 3.5, 3.6, 3.7, 3.8

```
cd tmp;
wget http://mag.gmu.edu/git-data/sblake/SCARR5_GM_IO2/IO2/3d__var_3_e20031120-070000-000.out.cdf
curl -O http://mag.gmu.edu/git-data/GaryQ-Physics/magnetosphere/kameleonV-0.1.0.tgz
tar zxvf kameleonV-linux-0.1.0.tgz
cd kameleonV-0.1.0
python kameleonV_test.py
```

See kameleonV_test.py for usage examples

# Compiling

## Step 1

```
cd /tmp
git clone https://github.com/rweigel/kameleon
```
Then read `kameleon/README.md` for instructions on dependencies

## Step 2

```
git clone https://github.com/rweigel/swig-and-ctypes
sudo apt install swig
cd swig-and-ctypes
make KAMELEON_DIR=/tmp
```

# Notes

Here SWIG was used, but perhaps this is easier donw with ctypes, e.g., https://stackoverflow.com/questions/5862915/passing-numpy-arrays-to-a-c-function-for-input-and-output

See end of the Makefile for description of why using the libraries from https://ccmc.gsfc.nasa.gov/Kameleon/Quick_start.html does not work.

# TODO:

1. Add function for field line tracing
2. `libccmc.so` (created by Step 1 in Compiling section above) depends on libhdf5 and libpython2.7. These libraries are not needed. 
3. Compile on OS-X
