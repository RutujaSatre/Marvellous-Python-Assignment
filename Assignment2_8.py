# Write a program which accept one number and display below pattern
# Input : 5
# Output :  1
#           1 2
#           1 2 3
#           1 2 3 4
#           1 2 3 4 5


def main():
    print("Enter the number : ")
    no=int(input())
    
    num = 1
    for i in range(0, no):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("")



if __name__=="__main__":
    main()