class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.coor=(self.x,self.y)

    def move(self,x,y):
        self.x += x
        self.y += y

    def __add__(self,p):
        return Point(self.x+p.x,self.y+p.y)

    def __sub__(self,p):
        return Point(self.x-p.x,self.y-p.y)

    def __mul__(self,p):
        return (self.x*p.x+self.y*p.y)   

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)         

    # comapare two Point so here defined the how comapare the point like distance from origin
    def __gt__(self,p):#greather than
        return self.length() > p.length()


    def __ge__(self,p):#greather equal to
        return self.length() >= p.length()

    def __lt__(self,p):#less than
        return self.length() < p.length()

    def __lt__(self,p):#less equal than
        return self.length() <= p.length()

    def __eq__(self,p):#equal to
        return self.x==p.x and self.y==p.y


    # this convert the representable formate when not this is then return any address 
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"


p1=Point(6,7)
p2=Point(5,6)    
p3=Point(6,8)
p4=Point(2,7)
# print(p1+p2): not add because don't added any method so here come dafault method pass
p5=p1+p2
p6=p1-p2
p7=p1*p2
print(p5,p6,p7)
print(p1==p2)
print(p1>p2)
print(p1>=p2)
print(p1<p2)
print(p1<=p2)
