# Write a program that takes user input for three numbers and prints the largest and smallest among them.
num1=eval(input("Enter first number: "))
num2=eval(input("Enter second number: "))
num3=eval(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >=num3:
    largest = num2
else:
    largest = num3
print(f"Largest Number is: {largest}")

if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3
print(f"Smallest Number is: {smallest}")

