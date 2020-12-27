lst1=[4,5,3,2,1]
lst2=[8,4,3,2,1,5,9]
print("lst1=",lst1)
print("lst2=",lst2)
a=len(lst1)
b=len(lst2)

if a==b:
    print("\nSAME LENGTH")
else:
    print("\nNOT SAME LENGTH")
    
s1=sum(lst1)
s2=sum(lst2)
if s1==s2:
    print("\nSUM IS SAME")
else:
        print("\nSUM IS NOT SAME")

lst1=set(lst1)
lst2=set(lst2)
i = lst1.intersection(lst2)
i=list(i)
print("\nCommon values:",i)
