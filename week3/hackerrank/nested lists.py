students = []
studentCount = int(input())

for i in range(studentCount):
    name = input()
    score = float(input())
    students.append({name: score})

# sort the list
students.sort(key=lambda item: list(item.values())[0])


# deleting the lowest score
lowestScore = list(students[0].values())[0]
students = list(filter(lambda item: list(item.values())[0] != lowestScore, students))

# sort again
students.sort(key=lambda item: list(item.values())[0])

# get the lowest ones
lowestScore = list(students[0].values())[0]
students = list(filter(lambda item: list(item.values())[0] == lowestScore, students))

# sort them by name
students.sort(key=lambda item: list(item.keys())[0])

# print names
for mark in students:
    print(list(mark.keys())[0])