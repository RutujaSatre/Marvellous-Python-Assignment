# Write aprogram which accept one number and display below pattern
# Input : 5 
# Output: * * * * *
#        * * * *
#        * * *
#        * *
#        *

def main():
    print("Enter number")
    val=int (input())

    for i in range(val, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")


if __name__=="__main__":
    main()