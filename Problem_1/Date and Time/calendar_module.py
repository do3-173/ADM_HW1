# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar


month, day, year = [int(x) for x in input().split()]

print(calendar.day_name[calendar.weekday(year, month, day)].upper())
