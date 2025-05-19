#Write a program which accept number from user and return addition of digits of that number

def main():
    print("Enter number : ")
    n = int(input())
    sum = 0

    while n > 0:
        sum = sum +  n % 10  
        n //= 10       # remove last digit

    print(sum)

if __name__=="__main__":
    main()