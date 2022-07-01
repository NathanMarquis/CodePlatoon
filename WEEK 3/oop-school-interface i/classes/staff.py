from classes.person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        Person.__init__(self, name, age, role, password)
        self.employee_id = employee_id

    def all_staff():
        with open("oop-school-interface i/data/staff.csv", newline='') as staff_file:
            reader = csv.DictReader(staff_file)
            arr_staff = []
            for row in reader:
                arr_staff.append(Staff(**row))
