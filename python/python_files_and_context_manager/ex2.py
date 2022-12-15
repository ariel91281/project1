def read_file(x):

    f = open('demofile.txt', 'r')
    list = f.readlines()
    print(list)
    for index, line in enumerate(list):
        if index == x:
            return
        print(line.replace('\n',''))
    f.close()

read_file(6)