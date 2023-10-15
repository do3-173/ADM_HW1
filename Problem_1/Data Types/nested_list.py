if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])

records.sort(key=lambda x: (x[1], x[0]))

second_lowest_grade = None

for student in records:
    if student[1] > records[0][1]:
        second_lowest_grade = student[1]
        break

second_lowest = [student[0] for student in records if student[1] == second_lowest_grade]

for student in second_lowest:
    print(student)
 