# Implement a program to calculate the area of complex shapes like a trapezoid or an ellipse.
import math

print ("................Area of Ellipse.................")
p=eval(input("Enter the value of semi-minor axis: "))
q=eval(input("Enter the value of semi-major axis: "))
ellipse= math.pi * p * q
print(f"Area is : {ellipse}")

print ("................Area of Trapezoid.................")
p=eval(input("Enter the value of longer base: "))
q=eval(input("Enter the value of shorter base: "))
h=eval(input("Enter the value of height: "))
trapezoid= 1/2 * (p+q) *h
print(f"Area is : {trapezoid}")



