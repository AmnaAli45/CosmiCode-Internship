# Create a program that generates the first 30 Fibonacci numbers using both iterative and recursive approaches.
print ("---------------------- Iterative Method ----------------------------")
first =0 
second = 1
print (first)
print (second)
for i in range (0,28):
    next = first + second
    print (next)
    first =second
    second = next

print ("---------------------- Recursive Method ----------------------------")
def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)
    

for i in range (30):
    print(fibonacci (i))