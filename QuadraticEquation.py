a = float(input("Enter first number"))
b = float(input("Enter second number"))
c = float(input("Enter third number"))

calculate = b**2 - 4*a*c

d = (-b + calculate**(1/2))/2*a
e = (-b - calculate**(1/2))/2*a

print("When positive", d)
print("When negetive", e)
