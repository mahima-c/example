from professor import Professor
from enroll import Enroll
class Course:
    def __init__(self,name,code,max_,min_,professor):
        self.name=name
        self.code=code
        self.max_=max_
        self.min_=min_
        self.professors=[]
        self.enrollments=[]


        if isinstance(professor,Professor):
            self.professors.append(professor)
        elif isinstance(professor,list):
            for entry in professor:
                if not isinstance(entry,Professor):
                    raise Error("Invalid professor..")
                self.professors=professor    
        else:
            raise Error("invalid professor")

    def add_professor(self,professor):
        if not isinstance(professor,Professor):
            raise Error("invalid professor")   

    def add_enroll(self,enroll):
        if not isinstance(enroll,Enroll):
            raise Error("invalid enroll")
        if len(enrollments) == self.max_:
            raise Error("course is full....")

        self.enrollments.append(enroll)

    def is_cancled(self):
        return len(enrollments) <= self.min_     