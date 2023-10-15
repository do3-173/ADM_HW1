# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n =np.array([int(x) for x in input().split()])

print(np.reshape(n,(3,3)))


