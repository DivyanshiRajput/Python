class Student:
    def __init__(self, name, rollNumber):
        self.name= name
        self.rollNumber= rollNumber
class Institute:
    students=[]
    def __init__(self, list):
        self.students = list

    def isStudentOf(self, s):
        if s in self.students:
            return True
        else:
            return False

    def isAddable(self, s):
        if s in self.students:
            return False
        else:
            return True

    def addStudent(self, s):
        if s in self.students:
            return False
        else:
            self.students.append(s)
            return True

