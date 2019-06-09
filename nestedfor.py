import random
student_ages = []
for i in range(100):
    student_ages.append(random.randint(10, 65))
print(student_ages)
for j in range(0, len(student_ages)):
    for i in range(j + 1, len(student_ages)):
        if student_ages[j] > student_ages[i]:
            temp = student_ages[j]
            student_ages[j] = student_ages[i]
            student_ages[i] = temp
print(student_ages)