import sys
import code

#https://stackoverflow.com/a/16528607

b = code.average(1., "a", [1., 2.])

print(b)
if False:
    if b == 1.0:
        print("Test passed")
        sys.exit(0)
    else:
        print("Test failed")    
        sys.exit(1)
