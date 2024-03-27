existing_list = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]

unique_list = set(existing_list)

new_list = list(unique_list)

descending_list = []

for i  in range (len(new_list) -1, -1, -1):
    descending_list.append(new_list[i])
print("This is descending list", descending_list)
