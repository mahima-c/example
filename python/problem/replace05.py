s=str(1004)
def replace(s):
    ns=""
    for ele in s:
        if ele=="0":
            ns+="5"
        else:
            ns+=ele    
    ans=int(ns)
    return ans

p=replace(s)  
print(type(p)) 



