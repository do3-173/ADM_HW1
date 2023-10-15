# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
np.set_printoptions(legacy = '1.13')

n, m = [int(x) for x in input().split()]

print(np.eye(n, m))
