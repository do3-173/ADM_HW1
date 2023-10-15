# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

pattern = r'^[4-6](?!.*(\d)([-\s_])\1)(?!.*(\d)\1{3,})\d{3}(-)?\d{4}(-)?\d{4}(-)?\d{4}$'


for _ in range(n):
    s = input()
    if re.match(pattern, s):
        print("Valid")
    else:
        print("Invalid")
