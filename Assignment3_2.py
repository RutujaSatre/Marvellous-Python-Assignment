# Write a program which accept  N numbers from user and store it into a list. Return Maximum number from that List

no = list(map(int, input("Enter numbers : ").split()))

max_number = max(no)

print("Maximum number :", max_number)
