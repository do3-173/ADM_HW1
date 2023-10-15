#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    solved = []
    capitalize_next = True
    for char in s:
        if char.isalpha():
            if capitalize_next:
                solved.append(char.upper())
                capitalize_next = False
            else:
                solved.append(char.lower())
        elif char.isspace():
            solved.append(char)
            capitalize_next = True
        else:
            solved.append(char)
            capitalize_next = False
    return ''.join(solved)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
