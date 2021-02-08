a=[2,5,3,87,12,3,2,0,88,21,34,7,11]
even_c, odd_c = 0, 0 
for num in a: 
	
	if num % 2 == 0: 
		even_c += 1

	else: 
		odd_c += 1
		
print("There are",even_c,"even numbers in the list") 
print("There are",odd_c,"Odd numbers in the list") 
