# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n, m, p = [int(x) for x in input().split()]

matrix_A = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix_A.append(row)

matrix_B = []
for _ in range(m):
    row = [int(x) for x in input().split()]
    matrix_B.append(row)
    
mat_A = np.array(matrix_A)
mat_B = np.array(matrix_B)

print(np.concatenate((mat_A, mat_B)))
