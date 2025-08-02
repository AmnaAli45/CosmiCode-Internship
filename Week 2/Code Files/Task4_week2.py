# Implement a program to find all the prime factors of a given number.
num = int (input("Enter a number:  "))
i = 2
while num > 1:
    if num % i == 0:
        print (i)
        num= num // i
    else:
        i = i+1

    
