input_list = [ 8,7,6,5,4,3,2,1]
sort = False
while sort == False:
    num_swap = 0
    for i in range(1, len(input_list)):
        if input_list[i-1] > input_list[i]:
            tmp = input_list[i-1]
            input_list[i-1] = input_list [i]
            input_list[i]=tmp
            num_swap = num_swap + 1
    if num_swap ==0:
        sort = True
    else:
        sort = False
    print ("This is the sorted list", input_list)

            
        
