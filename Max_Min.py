N = int(input("Enter the number of list: "))
numbers = []
for i in range(0, N):
    num = int(input("Enter the number : "))
    numbers.append(num)
max_num = max(numbers)
min_num = min(numbers)

print("this is the list: ", numbers)
print("Maximum number: ", max_num)
print("Minimum number: ", min_num)
