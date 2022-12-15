class PasswordError(Exception):
    pass



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

    errors = []
    if not passlen:
        errors.append("Too few characters")
    if not upper:
        errors.append("No uppercase letter")
    if not lower:
        errors.append("No lowercase letter")
    if not digit:
        errors.append("No digit")
    if not special_c:
        errors.append("No special character")

    error_res = ""
    if len(errors) == 1:
        error_res = "Password error: "
    else:
        error_res = "Password errors: "
    for error in errors:
        error_res += error + " "

    raise PasswordError(*errors)
