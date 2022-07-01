from classes.person import Person
import csv

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        Person.__init__(self, name, age, role, password)
        self.school_id = school_id

    def __str__(self):
        return f'{self.name}{self.age}{self.role}{self.school_id}{self.role}.'

    def all_students():
        with open("oop-school-interface i/data/students.csv", newline = '') as student_file:
            reader = csv.DictReader(student_file)
            arr_students = []
            for row in reader:
                arr_students.append(Student(**row))
        return arr_students
# print(Student.student_info)

