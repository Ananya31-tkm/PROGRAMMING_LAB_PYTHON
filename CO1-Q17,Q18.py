dict ={'Swathi':67,'Anu':98,'Riya':66,'Vismaya':88,'Neema':75,'Reshma':89}
import operator
dict1=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
print("Descending order:",dict1)
dict1=sorted(dict.items(),key=operator.itemgetter(1),reverse=False)
print("Ascending order:",dict1)
