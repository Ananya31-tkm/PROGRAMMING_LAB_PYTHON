st1="Good Morning""\n""Have a Nice Day""\n""Are you okay ?""\n"
fw=open("Afile.txt","w")
fw.write(st1)
fw.close()

fr=open("Afile.txt","r")
c=0
fr.seek(0)
s=fr.readlines()
for i  in s:
    c=c+1
    print(i)
print(len(s))
