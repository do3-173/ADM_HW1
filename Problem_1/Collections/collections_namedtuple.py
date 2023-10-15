# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple('students', columns)
print(f"{sum(float(Student(*input().split()).MARKS) for _ in range(n)) / n:.2f}")
