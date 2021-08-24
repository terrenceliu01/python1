import json

class Student:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def __repr__(self):
        return self.id

with open('data/student.json') as f:
    students = json.load(f)

print(type(students))
studentList = [Student(student['firstname'], student['lastname'], student['id']) for student in students]
print(studentList)
