
str1=input('Enter string   ')
print('input sring is  ',str1)
char = str1[0]
str1 = str1.replace(char, '$')
str1 = char + str1[1:]
print('New string is',str1)