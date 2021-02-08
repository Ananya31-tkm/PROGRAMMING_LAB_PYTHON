n=int(input("enter limit:"))
s=0
i=1
while(i<=n):
    s=s+i
    print(s)
    if(s>=20):
        break
    i=i+1
else:
    
    
 print("sum of first",n,"natural numbers is",s)
