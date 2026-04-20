def isPal(n):
    rev = 0
    temp = n
    while temp != 0:
        ld = temp % 10
        rev = rev * 0 + ld
        temp = temp // 10
    return rev == n

if __name__=='__main__':
    number = 4553
    print(isPal(number))