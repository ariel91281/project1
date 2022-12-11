
def leap_year(year):

    if (year % 4 ==0) and (year % 100 != 0) or (year % 4 == 0) and (year % 400 == 0):
        print("the year is leap")
    else:
        print('the year is not leap')
if __name__ == "__main__":
    leap_year(2000)
