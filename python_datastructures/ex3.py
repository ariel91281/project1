def both(list1, list2):
    share = []
    for i in list1:
        if i in list2:
            share.append(i)
    return share
x = both([1,2,3,4,5,6,7,8,256],[1,2,3,4,5,6,7,8,9,10,11,12])
print(x)