f = open("A.txt",'r')
str1 = f.readlines()
f.close()
f = open("B.txt",'w')
x = 0;
for i in str1:
    x = x+1
    if x%2!=0:
        f.write(i)
f.close()
f=open("B.txt",'r')
str2=f.readlines()
print(str2)
