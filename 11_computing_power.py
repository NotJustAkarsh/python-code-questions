# Naive Approach

def power(x, n):
    res = 1
    for i in range(n):
        res = res * x  # Time Complexity : θ(n)
    return res

# Optimized Approach 

def power(x, n):
    if n == 0:
        return 1
    temp = power(x,n//2)
    temp = temp * temp  # Time Complexity : O(log n)
    if(n%2 == 0):
        return temp
    else :
        return temp * x
    

print(power(3,5))