from classes.person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        Person.__init__(self, name, age, role, password)
        self.employee_id = employee_id

    def staff_info():
        with open("data/staff.csv", "r") as staff_file:
            reader = csv.DictReader(staff_file)
            arr_students = []
            for row in reader:
                arr_students.append(Staff(**row))
