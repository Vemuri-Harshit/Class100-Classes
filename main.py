class Student:
        def __init__(self, name, grade, rollNo):
            self.name = name self.grade = grade self.rollNo = rollNo

        def info(self):
            print("Hi " + self.name + " Of " + self.grade + " With Roll Number " + self.rollNo )

name_of_student = input("Name: ")
grade_of_student = input("Grade: ")
rollNo_of_student = input("RollNo: ")
harshit = Student(name_of_student, grade_of_student, rollNo_of_student)
harshit.info()                