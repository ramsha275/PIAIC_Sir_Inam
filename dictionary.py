# student = ["Alina", 90590435903, "90", "Sir Adnan"]
student = {
    'Name': 'Inam',
    'Cell Number': [90590435903, 86868687, 98798798],
    'Area': '90',
    'children': [{'ChildName': 'Ahmed', 'Age': 12, 'Address': 'Home'}, {'ChildName': 'Aisha', 'Age': 14, 'Address': 'Home'}],
    'Father Name': 'M Jaffar' 
}

print(student['children'][0]['ChildName'])
# for k in student:
#     print(student[k])
# arr = {
#     0: 1,
#     1: 2
# }
# student['Name'] = 'Alina Adnan'
# student['Module'] = 'Module 1'
# #del student['Area']
# print(student['Name'])
# print(student.pop('Area'))
students = []
print('Cuurently Enrolled Students: ', len(students))

for i in range(2):
    student = {}
    student['Name'] = input('Please Enter Student Name: ')
    student['Father Name'] = input('Please Enter Father Name: ')
    student['Cell Number'] = input('Please Enter Cell Number: ')
    students.append(student)
print('Cuurently Enrolled Students: ', len(students))

for idx in range(len(students)):
    if students[idx]['Name'].lower == 'inam':
        del students[idx]
print(students)
