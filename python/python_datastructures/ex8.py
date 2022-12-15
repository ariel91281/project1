def find_max_min(dictionary):
    lst_values = list(dictionary.values())
    lst_keys = list(dictionary.keys())
    dict_min = min(lst_values)
    dict_max = max(lst_values)

    print("the key of min is :",  lst_keys[lst_values.index(dict_min)])
    print("the key of max is :",  lst_keys[lst_values.index(dict_max)])

testing_dict = {"1": 3, "2": 4, "3": 1,"4": 2, "5": 9 }
find_max_min(testing_dict)