'''
****************************STUDENT MANAGEMENT SYSTEM*************************
**This Program Adds, Deletes and Seraches a student from in-memory list repository**
'''
students = []
while True:
    print('Press 1 to add student')
    print('Press 2 to find student')
    print('Press 3 to delete student')
    print('Press 4 to Exit!')
    print('Press 5 to check number of students enrolled!')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        student = {}
        student['Name'] = input('Please Enter Student Name: ')
        student['Father Name'] = input('Please Enter Father Name: ')
        student['Cell Number'] = input('Please Enter Cell Number: ')
        students.append(student)
    elif choice == 4:
        break
    elif choice == 5:
        print('We currently have ' + str(len(students)) + ' Students')
    elif choice == 2:
        name = input('Enter the name you want to search for! ')
        for student in students:
            if student['Name'].lower() == name.lower():
                print('Student with name ' + name + ' found and details are as follows!')
                print(student)