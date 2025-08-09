# Write a program to sort a list of integers using merge sort.
def mergeSort(arr,start,end):
    
    mid = int(start +((end-start)/2))
    if start < end:
        mergeSort(arr,start,mid) # Dividing into Left Half
        mergeSort(arr,mid+1,end) # Dividing into Right Half
        merge(arr,start,end,mid) #Merging
    return arr

# Merge Function
def merge(arr,start,end,mid):
    i = start #to track left half array
    j = mid + 1 #to track right half array
    temp=[] 
    while i <= mid and j <= end:
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
          temp.append(arr[i])
          i += 1
    while j <= end:
          temp.append(arr[j])
          j += 1
    
    for indx in range (len(temp)): # copying temp into original array
         arr[start+indx] = temp[indx]
   

arr=[12,31,35,8,32,17]
print(">>>>>>>>>>>>>>>>>>>>>>>>> Unsorted Array <<<<<<<<<<<<<<<<<<<<<<<<<")
print(arr)
print(">>>>>>>>>>>>>>>>>>>>>>>>> Sorted Array <<<<<<<<<<<<<<<<<<<<<<<<<")
print(mergeSort(arr,0,len(arr)-1))



