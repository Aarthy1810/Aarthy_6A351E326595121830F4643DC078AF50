print("Factorial")
n=int(input("Enter a number:"))
def factorial(n):
     if n==1:
         return 1
     else:
        return (n*factorial(n-1))
print("factorial of",n,"is :",factorial(n))