#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
sentence_list = [matrix[i][j] for j in range(len(matrix[0])) for i in range(len(matrix))]
    
sentence =  ''.join(map(str, sentence_list))

pattern = r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])'

print(re.sub(pattern, ' ', sentence))
