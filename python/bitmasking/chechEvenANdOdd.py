# concept is that first we assume no in bit if last digit is one then it's odd else even
# so we take and operation with 1 so that we find last digit
def checkEO(n):
    if(n & 1):
        print("Odd")

    else:
        print("even")   

n=3
checkEO(n)         
