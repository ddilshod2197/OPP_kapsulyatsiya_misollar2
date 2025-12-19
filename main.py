class Student:
    def __init__(self, name):
        self.name = name     
        self.__grades = []     

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("Baho 0-100 oralig‘ida bo‘lishi kerak!")

    def get_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def get_grades(self):
        return self.__grades


student = Student("Dilshod")

student.add_grade(85)
student.add_grade(90)
student.add_grade(110)  

print("Baholar:", student.get_grades())
print("O‘rtacha baho:", student.get_average())
