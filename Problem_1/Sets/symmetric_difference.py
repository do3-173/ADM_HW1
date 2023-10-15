# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
m_set = set(map(int,input().split()))
n = int(input())
n_set = set(map(int,input().split()))

difference = n_set.difference(m_set).union(m_set.difference(n_set))


difference_list = sorted(difference)

for diff in difference_list:
    print(diff)
