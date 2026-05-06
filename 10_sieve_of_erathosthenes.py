# Naive Approach

def isPrime(n):
    if n == 1 :
        return False
    if n == 2 or n == 3 :
        return True
    if n % 2 == 0 or n % 3 == 0 :
        return False
    i = 5

    while (i**0.5 <= n):
        if n % i == 0 or n %(i+2) == 0 :
            return False
        i += 6

    return True

def printPrimes(n):
    for i in range (2,n+1):
        if isPrime(i):
            print(i, end = " ")

# Optimized Approach

def sieve(n):
    if n <= 1:
        return
    
    isPrime = [True] * (n + 1)

    i = 2

    while i * i <= n :
        if isPrime[i]:
            for j in range(2 * i, n + 1, i):
                isPrime[j] = False

        i += 1

    for i in range(2, n+1):
        if isPrime[i]:
            print(i, end = " ")


# More Optimized Way

def sieve(n):

    if n <= 1:
        return 
    
    isPrime = [True] * (n + 1)

    i = 2
    while i <= n:
        if isPrime[i]:
          print(i, end = " ")

          for j in range (i*i, n+1 , i):
             isPrime[j] = False

        i += 1
if __name__ == "__main__":
    n = 18

    sieve(n)

