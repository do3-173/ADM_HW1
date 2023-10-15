# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())
arrow = '' 
for i in range(n//2):
    arrow = '.|.'*(2*i+1)
    print(arrow.center(m,'-'))
    
print('WELCOME'.center(m,'-'))


for i in range(n//2-1,-1,-1):
    arrow = '.|.'*(2*i+1)
    print(arrow.center(m,'-'))
        
  
