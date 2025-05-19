# Write a program which accept  N numbers from user and store it into a list. Return Minimum number from that List

no = list(map(int, input("Enter numbers : ").split()))

min_number = min(no)

print("Maximum number :", min_number)