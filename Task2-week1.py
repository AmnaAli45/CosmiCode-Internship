# Create a program to perform advanced arithmetic  operations (power, modulo) using functions.
def modulo (num1, num2):
    return num1 % num2
def power (base,pow):
    return base ** pow

print("...................MODULO........................")
number1=int(input("Enter first number for modulo: "))
number2=int(input("Enter second number for modulo: "))
mod=modulo(number1,number2)
print(f"modulo of {number1} and {number2} is: {mod}")

print("...................POWER........................")
number1=int(input("Enter base value : "))
number2=int(input("Enter exponent value : "))
p=power(number1,number2)
print(f"{number2} power of {number1} is: {p}")

