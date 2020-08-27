def Powerxn(x,n):
    if n==1:
        return 1
    smalloutput=Powerxn(n-1)
    return x*smalloutput

i=input()
x,n=int(i.split())

print(Powerxn(x,n))