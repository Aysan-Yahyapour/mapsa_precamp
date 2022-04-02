studentCount = int(input('enter:'))
studentMarks = []
for i in range(studentCount):
    lstSplitedStudent = input().split()
    studentMarks.append(lstSplitedStudent)

name = input('enter:')

for std in studentMarks:
    if name == std[0]:
        sum = 0
        for score in std[1:]:
            sum += int(score)
        print(sum / len(std[1:]))