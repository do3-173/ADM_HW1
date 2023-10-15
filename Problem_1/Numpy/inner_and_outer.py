# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

row_A = [int(x) for x in input().split()]
row_B = [int(x) for x in input().split()]

arr_A = np.array(row_A)
arr_B = np.array(row_B)

print(np.inner(arr_A, arr_B))
print(np.outer(arr_A, arr_B))
