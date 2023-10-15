# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n = tuple(int(x) for x in input().split())

print(np.zeros(n, dtype = np.int))
print(np.ones(n, dtype = np.int))
