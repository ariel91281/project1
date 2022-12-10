def sort_string(testing_str):
    result = sorted(testing_str, key=lambda item: int(item))
    print(result)

list = [12,32,256,38,1024,2]
sort_string(list)