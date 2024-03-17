m = int(input("Enter a number:"))
n = int(input("Enter a number"))

if (m<n):
        tmp = m
        m = n
        n = tmp

#print(m,n)

r = 1

while (r>0):
    r = m % n
    if ( r != 0):
        m = n
        n = r
    else:
        print("The gcd is", n )
        
