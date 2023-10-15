# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
np.set_printoptions(legacy='1.13')

a = [float(x) for x in input().split()]
arr = np.array(a, dtype=np.float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
