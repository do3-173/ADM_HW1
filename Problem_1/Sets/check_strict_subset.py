# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int,input().split()))
n = int(input())

for i in range(n):
    n_set = set(map(int,input().split()))
    if not A.issuperset(n_set):
        print("False")
        break
    if i == n - 1:
        print("True")
