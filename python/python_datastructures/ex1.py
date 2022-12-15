def return_str_list(mylist):
    helper = []
    for i in mylist:
        if type(i) != str:
            helper.append(i)
    for i in helper:
        mylist.remove(i)
mylist = ["france","argentina","england",5,12]
return_str_list(mylist)
print(mylist)

