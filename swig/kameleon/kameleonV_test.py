import sys
import numpy as np
import kameleonV

print("Python " + sys.version.replace("\n", ""))
fname = '/tmp/3d__var_3_e20031120-070000-000.out.cdf'

x = [1., 2.]
y = [1., 2.]
z = [1., 2.]
x1 = kameleonV.interpolate(fname, x, y, z, 'p')

x = np.array(x)
y = np.array(y)
z = np.array(z)
x2 = kameleonV.interpolate(fname, x, y, z, 'p')

assert(np.all(np.array(x1) == x2))

sys.exit(0)
