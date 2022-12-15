def remove_and_print(list2):
    while len(list2):
        list2 = list2[1::2]
        print(list2)

list2 = [1,2,3,4,5,6,7,8,9,10]
remove_and_print(list2)

