class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("hello i am",self.name,"and i am ",self.age,"year old") 

    def change_age(self,age):
        self.age=age    


    def add_weight(self,weight):
        self.weight=weight     


    def talk(self):
        print('bark!')      

mg=Dog("Mg",20)
mg.speak()
mg.change_age(190)
print(mg.age)
mg.add_weight(40)


# tutorial3(inheritance)
# lets craete cat class which have same and some addtional attribute as dog class when we don know about programming the basically we can copy the code
class Catt(object):
    def __init__(name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("hello i am",self.name,"and i am ",self.age,"year old") 
        
#this is not good because programmer don't copy the code,so we use here concept of inheritance
class Cat(Dog):
    # here cat is as child class and dog is parent classs it is derive forr dog class
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.name="tech"
        self.color=color

        # but we want to change the method of parent class then override the method
    def talk(self):
        print("meow!")
 

cat1=Cat("cat2",20,"blue")
print(cat1.name)
cat1.talk()
