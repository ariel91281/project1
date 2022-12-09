def unique(mydict):
    filt = set(list(mydict.values()))
    return filt



cars = {
    "company": "honda",
    "model": "crv",
    "year": 2013,
    "year1": 2013
}
print(unique(cars))


