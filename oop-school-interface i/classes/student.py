from classes.person import Person
import csv

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        Person.__init__(self, name, age, role, password)
        self.school_id = school_id

    def student_info():
     with open("data/students.csv", "r") as student_file:
            reader = csv.DictReader(student_file)
            arr_students = []
            for row in reader:
                arr_students.append(Student(**row))