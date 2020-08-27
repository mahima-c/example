# fib series:1 1 2 3....
def fib(n):
    if n==1 or n==2:
        return 1
    fib_1=fib(n-1)
    fib_2=fib(n-2)
    output=fib_1+fib_2
    return output
import sys
sys.setrecursionlimit(11000)
print(fib(2000))