# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n, m = [int(x) for x in input().split()]

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(np.array(row))
    
mat = np.array(matrix)
print(np.prod(np.sum(mat,axis = 0)))
