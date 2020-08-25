#classmethod,staticmethod and class variable
class Dog(object):
    # when we define class variable then it is at top
    dogs=[]
    def __init__(self,name):
        self.name=name
        self.dogs.append(self)


    @classmethod
    # mainly it is used for class variable,and when get something though class so don't need any instance
    def nums_dogs(cls):
        return len(cls.dogs)


    @staticmethod #it is called decorator
    # it is little diffrent here we can pass any arguments,and it also call direclty
    def bark(n):
        for i in range(n):
            print("bark!")

Dog.bark(4)   
print(len(Dog.dogs))         