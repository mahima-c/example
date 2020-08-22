# in python nothing is like public and private
# in python we repersent private as _name
class _private:
    def __init__(self,name):
        self.name=name

class NotPrivate:
    def __init__(self,name):
        self.name=name
        self.priv=_private(name)

    def _display(self):
        print("hello")  

    def _display(self):
        print("hi")  

'''
Public Access Modifier
Protected Access Modifier
Private Access Modifier   '''        
# Protected Access Modifier:
# The members of a class that are declared protected are only accessible to a class derived from it. Data members of a class are 
# declared protected by adding a single underscore ‘_’ symbol before the data member of that class.
class Student: 
     
     # protected data members 
     _name = None
     _roll = None
     _branch = None
     
     # constructor 
     def __init__(self, name, roll, branch):   
          self._name = name 
          self._roll = roll 
          self._branch = branch 
     
     # protected member function    
     def _displayRollAndBranch(self): 
  
          # accessing protected data members 
          print("Roll: ", self._roll) 
          print("Branch: ", self._branch) 
  
  
# derived class 
class Geek(Student): 
  
       # constructor  
       def __init__(self, name, roll, branch):  
                Student.__init__(self, name, roll, branch)  
          
       # public member function  
       def displayDetails(self): 
                    
                 # accessing protected data members of super class  
                print("Name: ", self._name)  
                    
                 # accessing protected member functions of super class  
                self._displayRollAndBranch() 
  
# creating objects of the derived class         
obj = Geek("R2J", 1706256, "Information Technology")  
  
# calling public member functions of the class 
obj.displayDetails()
# Private Access Modifier:
# The members of a class that are declared private are accessible 
# within the class only, private access modifier is the most secure access modifier. Data members of a class are declared private by adding a double 
# underscore ‘__’ symbol before the data member of that class.
class Geek: 
     
     # private members 
     __name = None
     __roll = None
     __branch = None
  
     # constructor 
     def __init__(self, name, roll, branch):   
          self.__name = name 
          self.__roll = roll 
          self.__branch = branch 
  
     # private member function   
     def __displayDetails(self): 
            
           # accessing private data members 
           print("Name: ", self.__name) 
           print("Roll: ", self.__roll) 
           print("Branch: ", self.__branch) 
     
     # public member function 
     def accessPrivateFunction(self):  
             
           # accesing private member function 
           self.__displayDetails()   
  
# creating object     
obj = Geek("R2J", 1706256, "Information Technology") 
  
# calling public member function of the class 
obj.accessPrivateFunction() 