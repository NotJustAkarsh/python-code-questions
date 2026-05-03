# Naive Approach

# def isPrime(n):
#     if n == 1 :
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# Optimised Approach 

# def isPrime(n):
#     if n == 1 :
#         return False
#     i = 2
#     while (i * i <= n):
#         if n % i == 0:
#             return False
#         i += 1
#     return True

# Super Optimised Approach 

def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3 :
        return True
    if n % 2 == 0 or n % 3 == 0 :
        return False
    i = 5
    while (i * i <= n):
        if n % i == 0 or n % (i + 2) == 0 :
            return False
        i += 6
    return True

if __name__ == "__main__":
    n = 47

    print(isPrime(n))