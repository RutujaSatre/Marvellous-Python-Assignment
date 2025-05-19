#Write a program which accept number from user and check whether number is prime or not

def main(): 
    no = int(input("Enter any number: "))

    if no > 1:
        for i in range(2, no):
            if (no % i) == 0:
                print("It is not a prime number : ",no)
                break
        else:
            print("It is a prime number : ",no)

if __name__=="__main__":
    main()