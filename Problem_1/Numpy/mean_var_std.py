# Enter your code here. Read input from STDIN. Print output to 

import numpy as np

n, m = [int(x) for x in input().split()]

matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(np.array(row, dtype = np.int))
    
mat = np.array(matrix)

print(np.mean(mat, axis=1))
print(np.var(mat, axis=0))
print(round(np.std(mat, axis=None),11))
