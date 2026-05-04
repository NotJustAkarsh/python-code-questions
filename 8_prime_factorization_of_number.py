def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def printPrimeFactors(n):
    for i in range(2, n + 1):
        if isPrime(i):
            while n % i == 0:
                print(i)
                n = n // i


printPrimeFactors(121)