n=int(input("enter number:"))
fact=1
if n<0:
    print("cannot find factorial")
elif n==0:
    print("Factorial is 0")
else:
    for i in range(1,n+1):
        fact=fact*i
print("Fctorial of ",n," is",fact)

    
