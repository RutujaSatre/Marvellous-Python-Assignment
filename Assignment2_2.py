# Write a program which accept one number and display below pattern
# Input :  5
#Output :  * * * * * 
#          * * * * *
#          * * * * *
#          * * * * *
#          * * * * *

def main():
    print("Enter the number: ")
    num=int(input())

    for i in range(0,num):
        for j in range(0,num):
            print("*",end=" ")
        print("")


if __name__=="__main__":
    main() 