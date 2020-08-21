from course import Course
from student import Student
from datetime import datetime

class Enroll:
    def __init__(self,student,course):
        if not isinstance(student,Student):
            raise Error("invalid student")
        if not isinstance(course,Course):
            raise Error("invalid course")
        self.student=student
        self.course=course
        self.grade=None
        self.date=datetime.now()


    def set_grade(self,grade):
        self.grade=grade    