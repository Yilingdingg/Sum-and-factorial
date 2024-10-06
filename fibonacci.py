n=int(input("Please enter a value:"))

def fib(n):
    if n==0 or n==1:
        return n
    elif n>1:
        return fib(n-1)+fib(n-2)
    
print("The fibonacci is", fib(n))