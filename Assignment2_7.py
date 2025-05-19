# Write aprogram which accept one number and display below pattern
# Input : 5
# Output :1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5


def main():
    print("Enter the number : ")
    no=int(input())
   
    for i in range(1, no+1):
        for j in range(1, no+1):
            print(j, end=" ")
           
        print("")



if __name__=="__main__":
    main()