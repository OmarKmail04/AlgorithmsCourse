def Factorial(n):
    if n==0:
        return 1
    else:
        return n*Factorial(n-1)
    
n=int(input())
print(Factorial(n))
