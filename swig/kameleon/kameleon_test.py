import _kameleon as kameleon
x = [1., 2.]
y = [1., 2.]
z = [1., 2.]
x = kameleon.runner('3d__var_3_e20031120-070000-000.out.cdf', x, y, z, len(x))
print(x)
