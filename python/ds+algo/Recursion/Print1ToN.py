def print1ToN(n):
    if n==0:
        return
    smalloutput=print1ToN(n-1)
    print(n)
    return


n=10
print1ToN(n)  #this print 1 to 10
    #   but we can print n to 1
def printNto1(n):
    if n==0:
        return
    print(n)
    smalloutput=printNto1(n-1) 
    return     

printNto1(n)      