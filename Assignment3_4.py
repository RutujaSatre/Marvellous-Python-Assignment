# Write a program which accept  N numbers from user and store it into a list. Accept one another number from user and return frequency of that number from list.

no = list(map(int, input("Enter numbers : ").split()))

val = int(input("Enter the number to find its frequency: "))

frequency = no.count(val)

print(f"Frequency of number in the list: ",frequency)
