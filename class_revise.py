class student():
    def __init__(self,name,age,rollno,gender):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.gender = gender

    def print_details(self):
        print("Name :",self.name,"Age :",self.age,"RollNo :",self.rollno,"Gender :",self.gender)


student1 = student("Umair", 21, "01", "Male")
student1.name = "Ammar"
student1.print_details()

