# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())
guests_rooms = list(map(int, input().split()))

unique_rooms = set()
duplicate_rooms = set()

for room in guests_rooms:
    if room not in unique_rooms:
        unique_rooms.add(room)
    else:
        duplicate_rooms.add(room)
        
print(unique_rooms.difference(duplicate_rooms).pop())
