# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = [int(x) for x in input().split()]
X = []
for _ in range(x):
    A = [float(x) for x in input().split()]
    X += [A]

for grades in zip(*X):
    print(sum(grades)/len(grades))
