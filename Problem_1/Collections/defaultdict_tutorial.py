
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = map(int, input().split())

a = defaultdict(list)
b = defaultdict(list)
for i in range(n):
    words = input()
    a[words].append(i + 1)
for i in range(m):
    words = input()
    b[i + 1].append(words)
    
for i in b.items():
    if i[1][0] not in a:
        print(-1)
    else:
        print(" ".join(map(str,a[i[1][0]])))
    