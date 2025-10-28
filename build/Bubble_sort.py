#Bubble Sort

def bubble_sort(arr):
    for j in range(len(arr)-1,-1,-1):
        for i in range(j):
            if arr[i]<arr[i+1]:
                continue
            else:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

arr = [13,45,65,23,45,34,62,78,27]
print(bubble_sort(arr))
