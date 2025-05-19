# Write a program which accept number from user and return addition of its factors

def sum(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total=total + i
    return total


number = int(input("Enter a integer: "))

if number > 0:
    result = sum(number)
    print(f"The sum of factors of is: ",result)
else:
    pass

