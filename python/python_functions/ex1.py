def rem_words(lst, some_words):
    result = list(filter(lambda word: word not in some_words, lst))
    print(result)

num_list = [10,22,33,40,50,60,70]
remove_list = [10,40,60]
rem_words(num_list, remove_list)