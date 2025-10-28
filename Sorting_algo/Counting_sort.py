#Counting Sort

def counting_sort(arr):
    n = len(arr)
    mx = max(arr)
    freq = [0] * (mx+1)
    for i in arr:
        freq[i] += 1
    res = []
    for i in range(mx+1):
        while freq[i] > 0:
            res.append(i)
            freq[i]-=1
    return res
arr = [13,45,65,23,45,13,34,62,78,27]
print(counting_sort(arr))
