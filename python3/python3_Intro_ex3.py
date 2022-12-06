def convert_temp(celsius):
    fahrenheit = (celsius * 1.8) + 32
    print(str(celsius )+ " degree Celsius is equal to " + str(fahrenheit )+ " degree Fahrenheit.")

if __name__ == "__main__":
    convert_temp(50)