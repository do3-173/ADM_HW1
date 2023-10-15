# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
for _ in range(t):
    n = int(input())
    n_blocks = [int(x) for x in input().split()]
    i = 0
    j = len(n_blocks) - 1
    while i < j:
        if n_blocks[i] < n_blocks[i+1] and n_blocks[j] < n_blocks[j-1]:
            print("No")
            break
            
        if n_blocks[i] >= n_blocks[i+1]:
            i += 1
            
        elif n_blocks[j] >= n_blocks[j-1]:
            j -= 1
            
        if i == j:
            print('Yes')
            break
        
        
