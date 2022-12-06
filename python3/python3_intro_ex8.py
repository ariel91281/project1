def PrimeNumber(num):
    if num>1:
        for i in range(2, num//2 +1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                return
        print(num, "is a prime number")

PrimeNumber(528)
