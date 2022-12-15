def discount_10(dict_testing):
    for key , value in dict_testing.items():
        dict_testing[key] = value * 0.9
    print(dict_testing)

dict_testing = {"mercedes": 500000, "honda": 60000, "mazda": 90000}
discount_10(dict_testing)