# Write a program which accept number from user and return its factorial

def main():
    print("Enter number:")
    no=int(input())
    Fact=1
    for i in range(1,no+1):
        Fact*= i
    print("Factorial : ",Fact)


if __name__=="__main__":
    main()