# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

pattern = r'^[789]\d{9}$'

for _ in range(n):
    s = input()
    if re.match(pattern, s):
        print("YES")
    else:
        print("NO")
    
