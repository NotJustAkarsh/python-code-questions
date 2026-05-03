# Naive Approach

def lcm(a,b):
    res = max(a,b)

    while True:
        if res % a == 0 and res % b == 0:
            return res
        res += 1
    return res

# Efficient Approach

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm (a,b):
    return a*b // gcd(a,b)  # LCM * HCF = Product of two numbers

if __name__ == "__main__":
    a = 4
    b = 6

    print(lcm(a,b))