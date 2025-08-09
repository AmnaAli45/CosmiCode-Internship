#Implement a program to check if a string is a palindrome, ignoring spaces and case sensitivity.
str=input("Enter the string: ")
str=str.lower()
palindrome = True
start = 0
end = len(str) -1

while start < end :
    if str[start] != str[end]:
        palindrome = False
        break
    start += 1
    end -= 1

if (palindrome):
    print("String is a valid palindrome")
else:
    print("String is not a valid palindrome")