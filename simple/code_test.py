import sys
import code

#https://stackoverflow.com/a/16528607

b = code.average(1., "a", [1., 2.])

assert(b == (1., 2.))
print("PASS")
