from functools import reduce

def calc_numbers(lst):
    result = reduce(lambda a, b: a+b, lst)
    print("the sum is : ", result)

lst_testing = [10,-12,30,-50,-255]
calc_numbers(lst_testing)