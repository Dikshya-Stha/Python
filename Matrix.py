a = [
    [24, 3, 6],
    [8, 12, 16],
    [2, 66, 7],
    ]
b = []
maxv= a[0][0]
minv = a[0][0]
for i in range ( len (a)):
    for j in range (len(a[i])):
        if a[i] [j] %2 == 0 and a[i] [j] % 3==0:
            b.append(a[i][j])
        
        if a[i] [j] >maxv:
            maxv = a[i][j]
            
        if a[i] [j] < minv:
            minv = a[i][j]
            
print("the number divisble by 2 and 3", b)

print("The maximum value is", maxv)

print("The minimum value is", minv)

