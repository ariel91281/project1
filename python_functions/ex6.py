def word_to_nume_value(testing_str):
    gematria_dict = {"א": 1, "ב": 2, "ג": 3, "ד": 4, "ה": 5, "ו": 6, "ז": 7, "ח": 8,
                     "ט": 9, "י": 10, "כ": 20, "ל": 30, "מ": 40, "נ": 50, "ס": 60, "ע": 70,
                     "פ": 80, "צ": 90, "ק": 100, "ר": 200, "ש": 300, "ת": 400, "ך": 500, "ם": 600,
                     "ן": 700, "ף": 800, "ץ": 900}

    calculate_value = 0
    for char in testing_str:
        if char in gematria_dict.keys():
            calculate_value += gematria_dict[char]
    return calculate_value

str_testing = "מודניאל"
str_another = "אירופה"
result = word_to_nume_value(str_another)
result2 = word_to_nume_value(str_testing)
print(result)
print(result2)