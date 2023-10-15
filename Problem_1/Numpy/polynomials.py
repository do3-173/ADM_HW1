# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

p = [float(x) for x in input().split()]

x = int(input())
print(np.polyval(p,x))
