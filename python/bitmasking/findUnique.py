# bitwise operator
# very fast
# find the uniques no in array,when every no occure twise except one 
# xor of two same no is cancle out each other
def findUniqueNo(arr):
    res=0
    for ele in arr:
        res=res^ele

    return res    

arr=[1,2,4,2,1]    
print(findUniqueNo(arr))