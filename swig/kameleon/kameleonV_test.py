import os
import sys
import numpy as np
import kameleonV

print("------------------------------------------------------------------------------")
print("Testing kameleonV in Python " + sys.version.replace("\n", ""))
print("------------------------------------------------------------------------------")

fname = '3d__var_3_e20031120-070000-000.out.cdf'
fpath = '/tmp/3d__var_3_e20031120-070000-000.out.cdf'

if not os.path.exists(fpath):
    print('Downloading ' + fname)
    os.system('cd /tmp; curl -O http://mag.gmu.edu/git-data/sblake/SCARR5_GM_IO2/IO2/' + fname)

x = [1., 2.]
y = [1., 2.]
z = [1., 2.]
x1 = kameleonV.interpolate(fpath, x, y, z, 'p')

x = np.array(x)
y = np.array(y)
z = np.array(z)
x2 = kameleonV.interpolate(fpath, x, y, z, 'p')

assert(np.all(np.array(x1) == x2))

print('\033[92m' + "PASS" + '\033[0m')
print("------------------------------------------------------------------------------")
sys.exit(0)
