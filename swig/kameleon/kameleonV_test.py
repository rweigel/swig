import os
import sys
import numpy as np
import kameleonV

print("------------------------------------------------------------------------------")
print("Testing kameleonV in Python " + sys.version.replace("\n", ""))
print("------------------------------------------------------------------------------")

fname = '3d__var_1_e20120723-120000-000.out.cdf'
fpath = '/tmp/' + fname

url = 'http://mag.gmu.edu/git-data/bcurtiswx/Differences/data/Sean_Blake_081318_1/GM_CDF/'
if not os.path.exists(fpath):
    print('Downloading ' + fname)
    os.system('cd /tmp; wget ' + url + fname)

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
