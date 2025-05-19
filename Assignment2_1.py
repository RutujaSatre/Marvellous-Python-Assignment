#Create on module named as Arithmetic which contains 4 functions as Add() for addition, sub() for Subtraction, Mult() for multiplication and Div() for division . All functions accepts two parameters as number and perform the operation . Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.


import Arithmetic


print("Enter First number : ")
num1=int(input())

print("Enter second number : ")
num2=int(input())

print(f"Addition: {Arithmetic.Add(num1, num2)}")
print(f"Subtraction: {Arithmetic.Sub(num1, num2)}")
print(f"Multiplication: {Arithmetic.Mult(num1, num2)}")
print(f"Division: {Arithmetic.Div(num1, num2)}")

    
