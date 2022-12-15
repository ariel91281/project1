import csv
def max_min_age(csvfile):
    with open(csvfile,'r') as file:
        csv_values1 = csv.reader(file)
        next(csv_values1)
        lista = [line for line in csv_values1]
        vaccinated = [int(line[1]) for line in lista if line[6] == "Y"]
        not_vaccinated = [int(line[1]) for line in lista if line[6] == "N"]

    print(max(vaccinated))

    print(min(vaccinated))

    print(max(not_vaccinated))

    print(min(not_vaccinated))

    Length_of_hospitalization = [int(line[4]) for line in lista]
    print(Length_of_hospitalization)
    average = sum(Length_of_hospitalization)/ len(Length_of_hospitalization)
    print(average)

def filt_choose(csvfile, fileinput):
    gender = input("which gender do you want: ")
    vaccinated = input("vaccinated or not vaccinated")
    min_age = input("choose the min age")
    max_age = input("choose the max age")
    with open(csvfile,'r') as file:
        csv_values1 = csv.reader(file)
        next(csv_values1)
        lista = [line for line in csv_values1]
        list_filter = [line for line in lista if line[0] == gender and  line[1] >= min_age  and  line[1] <= max_age  and line[6] == vaccinated]
    with open(fileinput, 'w') as file:
        file.write(str((list_filter)))
        print(list_filter)


max_min_age("/home/ariel/Downloads/corona.csv")
filt_choose("/home/ariel/Downloads/corona.csv","/home/ariel/Downloads/filtercorona.txt")
