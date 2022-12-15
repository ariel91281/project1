def check_complexity():
    password = input("Input password: ")
    digit = False
    upper = False
    lower = False
    special_c = False
    passwordlen = False
    if len(password) > 7:
        passwordlen = True
    for character in password:
        if character.isupper():
            upper = True
        if character.islower():
            lower = True
        if character.isdigit():
            digit = True
        if password.count('@') > 0 or password.count('#') > 0 or password.count('%') > 0 or password.count('&') > 0:
            special_c = True
        if lower and upper and digit and special_c and passwordlen:
            print("Password is good")
            return True
