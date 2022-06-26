from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def __str__(self):
        str = f'''
        {self.student.name}
        ---------------
        age: {self.student.age}
        id:{self.student.school_id}
        '''
        return str

    def list_students(self):
        self.counter = 1
        for student in self.students:
            print(f"{self.counter}. {student.name} {student.school_id}")
            self.counter += 1
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student.name

