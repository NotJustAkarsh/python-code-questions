# Naive Approach

def printDivisors(n):
    for i in range(1,n+1):
        if (n % i == 0):
            print(i)

# Optimized but not in order
def printDivisors(n):
    i = 1
    while (i*i<=n):
        if(n%i == 0):
            print(i)
            if(i!=n/i):
                print(n//i)
        i+=1
        

# Optimized and in order
def printDivisors(n):
    i = 1
    while(i*i < n):
        if(n%i == 0):
            print(i)
        i+=1
    while (i>=1):
        if (n%i == 0):
            print(n//i)
        i -= 1
            
print(printDivisors(18))