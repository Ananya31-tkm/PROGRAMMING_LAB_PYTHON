a1 ={'Swathi':67,'Anu':98,'Riya':66,'Vismaya':88,'Neema':75,'Reshma':89}
print("Inputed dict is :", a1)
a1_sorted_keys = sorted(a1, key=a1.get, reverse=True)
a1_sorted_keys_2 = sorted(a1, key=a1.get)

print("Descending order:",a1_sorted_keys)
print("Ascending order:",a1_sorted_keys_2)
