# extract i th bit not
# build the mask
# 4=100,mask=1<<i
def getIthBit(n,i):
    mask=(1<<i)#left shift
    ans=n & mask 
    # if bit is set then find positive no else bit is reset than it's zero
    # 13:1101 lets find 2nd bit,mask=0100 ans =all bit set to zero as take and operator
    if(ans):
        return 1
    else:
        return 0   

#set ith bit
def setIthBit(n,i):
    mask=1<<i 
    n=(n | mask) 

    return n
print(setIthBit(4,1))

# clear ith bit
def clearIthBit(n,i):
    mask= ~(1<<i)
    n=n & mask

    return n 
print(clearIthBit(4,2))     