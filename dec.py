
def DecimalToBinary(num):
	
	if num >= 1:
		DecimalToBinary(num // 2)
	print(num % 2, end = '')

def DecimalToOct(num):
    if num>0:
        DecimalToOct((int)(num/8))
        print(num % 8,end=' ')

def DecimalToHex(n):
    num=hex(n)
    print(num)



num=int(input("Enter any decimal value:"))
print("\nBinary equivalent is:")
DecimalToBinary(num)
print("\nOctal equivalent is:")  
DecimalToOct(num)
print("\nHexadecimal equivalent is:")
DecimalToHex(num)
