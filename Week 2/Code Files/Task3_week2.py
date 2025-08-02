# Write a function to calculate the greatest common divisor (GCD) and least common multiple (LCM) of two numbers.

def gcd(a,b):
    
    if  b <= a:
        x,y = a,b
    else:
        x,y = b,a
    while y != 0:
        x , y = y, x % y
    return x

def lcm(a,b):
    return (a*b)//gcd(a,b)

a = int (input ("Enter First Number: "))
b= int (input ("Enter Second Number: "))
print ("--------------------------- Greatest Common Divisor (GCD) --------------------")
print (gcd(a,b))
print ("--------------------------- Least Common Multiple (LCM) --------------------")
print (lcm(a,b))