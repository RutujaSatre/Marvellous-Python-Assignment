# program to check wheather number is positive , negative or zero
def main():
    print("Enter Number: ")
    no=int(input())

    if(no>0):
        print("Positive Number")

    elif(no==0):
        print("zero")

    else:
        print("Negative Number")

if __name__=="__main__":
    main()
