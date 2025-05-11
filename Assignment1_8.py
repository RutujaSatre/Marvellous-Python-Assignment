#Program which accept number from user and print that number of "*" on screen
def StarPattern():
    print("Enter Number:")
    num=int(input())

    if(num>0):
        print("*"*num)
    else:
        pass



if __name__=="__main__":
    StarPattern()
