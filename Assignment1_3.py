def Add(no1,no2):
    result=no1+no2
    return result

def main():
    print("Enter First no: ")
    value1=int (input())

    print("Enter Second no: ")
    value2=int(input())

    ans=Add(value1,value2)
    print("Answer is: ",ans)


if __name__=="__main__":
    main()