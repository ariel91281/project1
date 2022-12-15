def PrimeNumber(num):
    if num > 1:
        for i in range(2, num//2 +1):
            if (num % i) == 0:
               return False
        return True




for i in range(2, 1000):
    if PrimeNumber(i):
        print(i)
