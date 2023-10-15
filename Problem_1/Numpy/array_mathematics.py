# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n, m = [int(x) for x in input().split()]

matrix_A = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix_A.append(np.array(row, dtype = np.int))

matrix_B = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix_B.append(np.array(row, dtype = np.int))

mat_A = np.array(matrix_A)
mat_B = np.array(matrix_B)

print(mat_A + mat_B)
print(mat_A - mat_B)
print(mat_A * mat_B)
print(mat_A // mat_B)
print(mat_A % mat_B)
print(mat_A ** mat_B)
