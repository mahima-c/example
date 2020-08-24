def largestAndSecondLargest(sizeOfArray, arr):
    
    if sizeOfArray == 1:
        return -1
        
    first=arr[0]
    second=-1        
    
    for i in range(1,sizeOfArray):
        if(arr[i]>first):   
            second=first
            first=arr[i]

        elif(arr[i]>second and arr[i]!=first):
            second=arr[i]
            
    if second != first:
        li=[first,second]     
    else:
        li=[first,-1]
    return li        
      