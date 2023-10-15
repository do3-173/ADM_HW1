# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

s = input()
k = input()

pattern = re.compile(re.escape(k))


if re.search(pattern, s):
    for i in range(0, len(s) - len(k) + 1):
        m = re.search(pattern, s[i:i+len(k)])
        if m:
            print(f"({m.start() + i}, {m.end() + i - 1})")
else:
    print(f"(-1, -1)")
