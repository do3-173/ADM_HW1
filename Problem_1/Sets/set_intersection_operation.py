# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
n_set = set(map(int,input().split()))
m = int(input())
m_set = set(map(int,input().split()))

print(len(n_set.intersection(m_set)))
