#Iterative Approach 

def fact(n):
    res = 1
    for i in range(2,n+1):
        res = res*i
    return res

if __name__ == "__main__":
    number = 5
    print(fact(number))


#Recursive Approach

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

if __name__ == "__main__":
    number = 5
    print(fact(number))


