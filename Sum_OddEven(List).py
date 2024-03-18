suppose = True
MyList = []

while suppose == True :
    take = int(input("Enter a number: "))
    MyList.append(take)

    ask = input ("If u want to end the number write 'no'")
    if ask == "no" or ask =="No":
        break

print(MyList)
oddnum = 0
evennum = 0

for elements in MyList:
    if elements % 2 != 0:
        oddnum = oddnum + elements
    else:
        evennum = evennum + elements
        
print("odd total are: ", oddnum)
print("even total are:", evennum)   
