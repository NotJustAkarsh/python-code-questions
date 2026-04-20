x = int(input("Enter any number to count the digits : "))
res = 0
while x > 0:
    x = x // 10
    res = res + 1
print(f"The count of the digits of {x} is {res}")