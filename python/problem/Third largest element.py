import sys
def thirdlargest(arr,n):
    first=arr[0]
    second=-(sys.maxsize)
    third=-(sys.maxsize)  
    for i in range(1,n-1):
        if(arr[i]>first):
            third=second
            second=first
            first=arr[i]

        elif(arr[i]>second):
            third=second
            second=arr[i]


        else(arr[i]>third):
            third=arr[i]
                     
    return third        
# print(sys.maxsize)