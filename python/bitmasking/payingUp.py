def filterChars(a,n0):
    i=0
    sum=0
    while(n0>0):
        if(n0 & 1):
            sum+=a[i]   
        i=i+1
        n0=n0>>1    
    return sum

def genratesubstring(a,k):
    #genrate the mask for 0 to 2^n-1
    dp=[]
    n=(1<<len(a))
    for i in range(1,n):
        sum=filterChars(a,i)
        dp.append(sum)

    for ele in dp:
        if ele==k:
            print("Yes")
            return 

    print("No") 
    return  

arr=[9,8,7,6,5,4,8,9,90]
genratesubstring(arr,99) 
        

