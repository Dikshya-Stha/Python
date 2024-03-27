new = {}
continueLoop = True
while continueLoop == True:
    name = input("Please enter your name: ")
    marks = int(input("Please enter your marks: "))

    new.update({name:marks})

    continuation = input("Do you want to continue? (Yes/No)")
    if continuation == "no" or continuation == "No":
            break
newl = list(new.values())
maxv = newl[0]
sumt = 0
for value in new.items():
    if  maxv < value:
        maxv = value
    

    sumt = sumt+value
avgl = sumt / len(newl)
    



