def decimal_to_conversion(dec): 
    decimal = int(dec) 
    print(decimal, " in Binary : ", bin(decimal))  
    decimal = int(dec) 
    print(decimal, "in Octal : ", oct(decimal))  
    decimal = int(dec) 
    print(decimal, " in Hexadecimal : ", hex(decimal))



dec=int(input("Enter the Decimal number:"))
decimal_to_conversion(dec)  
