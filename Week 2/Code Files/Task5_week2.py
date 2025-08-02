# Write a program that takes a list of numbers and finds the subarray with the maximum sum (Kadane's Algorithm).
arr=[]
n=int(input("Enter the length of array: "))
for i in range (0,n):
    value = int (input("Enter the value: "))
    arr.append(value)

max_sum= arr[0]
max_end=arr[0]
start=end=s=0
for i in range(0,n):
    if arr[i] > max_end + arr[i]:
        max_end = arr[i]
        s=i
    else:
        max_end +=arr[i]
    if max_end > max_sum:
        max_sum = max_end
        start = s
        end = i

max_subarray=arr[start:end+1]
print ("--------------- MAX SUM IS -----------------")
print(max_sum)
print("------------ Sub Array is ------------------")
print(max_subarray)