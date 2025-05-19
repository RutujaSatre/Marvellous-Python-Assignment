# Write a program which accept  N numbers from user and store it into a list. Return addition of all elements from that List

def main():
    print("Enter number of elements: ")
    number=int(input())

    Data =[]

    print("Enter the values")
    for i in range(number):
        no=int(input())
        
        Data.append(no)

    Sum= sum(Data)
    print()


if __name__=="__main__":
    main()