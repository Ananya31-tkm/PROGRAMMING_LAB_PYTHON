a=int(input("Enter first num:"))
b=int(input("Enter second num:"))
if a > b:
    x = a
else:
    x = b

for i in range(1, x):
    if a % i == 0 and b % i==0:
        hcf = i

print ("hcf of both is: ", hcf)

for j in range(x, a * b):
    if j % a == 0 and j % b == 0:
        lcm = j
        break       

print ("lcm of both is: ", lcm)
