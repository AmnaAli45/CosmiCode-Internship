# Write a program to check if a number is prime, and also list all prime numbers up to that number.
num=int(input("Enter a value: "))
prime=True
for i in range (2,num):
    if num % i == 0:
        prime = False
        break

if prime:
    print("The given number is a prime number.")
else:
    print("The given number is not a prime number.")

print("--------------- All Prime Numbers -----------------")
primes=[]
for i in range (1,num+1):
    prime= True
    for j in range (2,i):
        if i % j == 0:
            prime = False
            break
    if prime:
            primes.append(i)
        
for i in primes:
    print (i)


