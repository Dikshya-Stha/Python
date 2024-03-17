num = int(input("Enter a number: "))
start = 2
count = 0
if num == 1 or num == 0:
    print("They are not prime or composite")
else:
    while start<num :
        if num % start == 0:
            count = 1
        start = start + 1
    if count == 0:
        print("Print")
    else:
        print("Not Prime")
