

def trans_money (sum_of_money):
    bank_notes = {}
    bank_notes.update({"200":sum_of_money//200})
    sum_of_money -= bank_notes["200"] * 200

    bank_notes.update({"100": sum_of_money // 100})
    sum_of_money -= bank_notes["100"] * 100

    bank_notes.update({"50": sum_of_money // 50})
    sum_of_money -= bank_notes["50"] * 50

    bank_notes.update({"20": sum_of_money // 20})
    sum_of_money -= bank_notes["20"] * 20

    bank_notes.update({"10": sum_of_money // 10})
    sum_of_money -= bank_notes["10"] * 10

    bank_notes.update({"5": sum_of_money // 5})
    sum_of_money -= bank_notes["5"] * 5

    bank_notes.update({"2": sum_of_money // 2})
    sum_of_money -= bank_notes["2"] * 2

    bank_notes.update({"1": sum_of_money // 1})
    sum_of_money -= bank_notes["1"] * 1
    return bank_notes




print( trans_money(10206))








