#Insertion_sort

def Insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr


arr = [13,45,65,23,45,13,34,62,78,27]
print(Insertion_sort(arr))
