# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pattern = r'([a-zA-Z0-9])\1'

s = input()

m = re.search(pattern, s)

if m:
    print(m.group(1))
else:
    print(-1)
