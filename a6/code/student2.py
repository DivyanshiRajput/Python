class Student:
    name= ""
    rollNumber=1
    def __init__(self, student):
        self.name= student
        self.rollNumber= Student.rollNumber
        Student.rollNumber+= 1



