def func1(str):
    mydict = {}
    myset = set(str)                                               #filter the str , avoid duplicates and contains unique  characters that apeared str
    for i in myset:                                                #iterate over myset instead of str
        mydict.update({i: str.count(i)})                           #update the dictionary with given a key value, if key doesnt exsits create new key and value
    return mydict

print(func1("englandfranceargentina"))
