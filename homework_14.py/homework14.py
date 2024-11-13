class Student:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_grade = 0
    
    def set_avg_grade(self, value):
        self.avg_grade = value

student_anna = Student(name='Anna', surname='Polovykh', age=26)
student_anna.set_avg_grade(80)
print(student_anna.name)
print(student_anna.surname)
print(student_anna.age)
print(student_anna.avg_grade)