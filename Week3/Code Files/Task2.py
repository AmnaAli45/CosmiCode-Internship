# Create a program that reverses a list without using builtin functions and prints both the original and reversed lists.
org_list = []
num = int(input("Enter the length of list: "))
for i in range (num):
    value = eval(input("Enter the list value: "))
    org_list.append(value)

start = 0
end = num - 1
rev_list=[0] * num 


for i in range (num):
        rev_list[end] = org_list[i]
        end -= 1

print("--------------Original List---------------------")
print(org_list)
print("--------------Reversed List---------------------")
print(rev_list)
