m = int(input("Enter the rows:"))
n = int(input("Enter thre columns:"))
d2d = []
for i in range(m):
    rowl = []
    for j in range(n):
        if i == j:
            rowl.append(1)
        elif i>j:
            rowl.append(3)
        else:
            rowl.append(2)
    d2d.append(rowl)
print(d2d)
            
        
            

            
    
