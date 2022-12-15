def what_is_vaild_card(number_str):
    second_numbers = number_str[-2::-2]
    first_numbers = number_str[-1::-2]

    lst_seconds_after_calc = []
    lst_firsts = []
    for item in second_numbers:
        current_value = int(item) * 2
        if current_value > 9:
            current_value = current_value - 9
        lst_seconds_after_calc.append(current_value)
    print(lst_seconds_after_calc)
    for first_item in first_numbers:
        lst_firsts.append(int(first_item))
    print(lst_firsts)

    lst_total = lst_firsts + lst_seconds_after_calc
    sum = 0
    for item in lst_total:
        sum +- item
    if sum % 10 == 0:
        return "valid"
    else:
        return "not valid"


print(what_is_vaild_card("4539319503043115"))
