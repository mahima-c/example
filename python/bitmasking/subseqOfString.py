# find subsequence of string
# abc:a,b,c,ab,bc,ac,abc
# no of substring=a(0,1)-2 same as b and c(2*2*2-1):0-7
#complexity=o(2^n-1)
def filterChars(a,n0):
    i=0
    while(n0>0):
        if(n0 & 1):
            print(a[i],end="")
        i=i+1
        n0=n0>>1    
    print() 
       

def genratesubstring(a):
    #genrate the mask for 0 to 2^n-1
    n=(1<<len(a))
    for i in range(1,n):
        # print("done2")
        filterChars(a,i)

genratesubstring("abc") 
# filterChars("abc",4)           

