# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n = int(input())

matrix = []
for _ in range(n):
    row = [float(x) for x in input().split()]
    matrix.append(np.array(row, dtype = np.float))
    
mat = np.array(matrix)
print(round(np.linalg.det(mat), 2))
