#program to check wheather number is even or odd
def ChkNum():
    print("Enter Number: ")
    value=int(input())

    if(value%2==0):
        print("Even Number")
    else:
        print("Odd Number")


if __name__=="__main__":
    ChkNum()
