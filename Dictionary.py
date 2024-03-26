new = {}
continueLoop = True
while continueLoop == True:
    name = input("Please enter your name:")
    marks = int(input("Please enter your marks:"))
    
    new.update({name:marks})

    continuation = input(" Do you want to continue? (Yes/No)")
    if continuation == "no" or continuation == "No":
        break

for key, value in new.items():
    print("Name of student is:", key,"and Marks obtained is:", value)
    
