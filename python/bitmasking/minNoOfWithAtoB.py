# find min no bit chenged,if no is a,b  a is changed to b by chnageing bit
# concept is that we take xor of both no, if both bit is similar than where 0 taken and else 1 
# and then find no of ones present 
def findNoOfSetBit(n):
    count=0
    while(n>0):
        count += (n&1)
        n=n>>1
    return count  #complexity is o(no of bit)      

a=1
b=6
def AtoB(a,b):
    res=a^b
    ans=findNoOfSetBit(res)
    print(ans)

AtoB(a,b)   
#method:2
# for finding no of set bit
def findNoOfSetBit2(n):
    count=0
    while(n>0):
        count=count+1
        n=n&(n-1)
    return count #complexity is o(no of set bit)    
        



















