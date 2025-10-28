# Google: Given an array of positive integers, a peak element is greater than its neighbors. 
# Write a function to find the index of any peak elements. 
# For example, for [3, 5, 2, 4, 1], you should 
# return either 1 or 3 because the values at those indexes, 5 and 4, are both peak elements.


def find_any_peak_element_linear(arr):
    res = []
    for i in range(len(arr)):      
        if i == 0:
            if arr[i]>arr[i+1]:
                res.append(i)
        elif i == len(arr)-1:
            if arr[i]>arr[i-1]:
                res.append(i)
        else:
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                res.append(i)
            else:
                continue
    return res

arr = [3, 5, 2, 4, 1]
print(find_any_peak_element_linear(arr))
