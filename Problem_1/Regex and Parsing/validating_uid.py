# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

pattern = r'(?!.*(.).*\1)(?=(?:[^A-Z]*[A-Z]){2})(?=(?:\D*\d){3})[A-Za-z0-9]{10}'
        

for _ in range(n):
    s = input()
    if re.match(pattern, s):
        print("Valid")
    else:
        print("Invalid")
