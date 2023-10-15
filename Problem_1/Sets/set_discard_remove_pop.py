# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
l = list(map(int,input().split()))
s = set()

for i in range(n - 1, -1, -1):
        s.add(l[i])
        
n = int(input())
for i in range(n):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    if command[0] == 'remove':
        s.remove(int(command[1]))
    if command[0] == 'discard':
        s.discard(int(command[1]))
    
print(sum(s))
