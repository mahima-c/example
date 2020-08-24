import sys
arr=[1,2,3,2]

n=4
x = 1
y = 2

def Minimumdistance(arr,x,y,n):
    i=0
    min_distance=sys.maxsize
    while i<n:
        j=i+1
        if (arr[i]==x or arr[i]==y):
            while j<n:
                if (arr[j]==x or arr[j]==y) and min_distance>abs(i-j):
                    min_distance=abs(i-j)
                    print(min_distance) 
                j=j+1             
        i=j
    if min_distance>n:
        return -1    
    return min_distance    

print(Minimumdistance(arr,x,y,n))