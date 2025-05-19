# Write a program which accept  N numbers from user and store it into a list.Return addition of all prime numbers from that List. Main python file accept N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as Marvellous. Name of the function from main python file should be ListPrime().

import Marvellous  

def main():
    no = list(map(int, input("Enter numbers separated by space: ").split()))

    prime = [num for num in no if Marvellous.ChkPrime(num)]

    sumPrime = sum(prime)

    print("Prime numbers:", prime)
    print("Sum of prime numbers:", sumPrime)


if __name__=="__main__":
    main() 