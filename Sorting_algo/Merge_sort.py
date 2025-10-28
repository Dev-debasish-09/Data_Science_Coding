#Merge_sort

def Merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        Merge_sort(left_arr)
        Merge_sort(right_arr)

        i = 0 #left arr index
        j = 0 # right arr index
        k = 0 # res arr indes

        while i<len(left_arr) and j<len(left_arr):
            if left_arr[i]<right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j+=1
            k += 1
        
        while i<len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j<len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr

arr = [13,45,65,23,45,13,34,62,78,27]
print(Merge_sort(arr))
