def xorSwaping(a,b):
    a=a^b
    b=b^a
    a=a^b

    return a,b  


c,d=xorSwaping(3,4) 
print(c,d)   