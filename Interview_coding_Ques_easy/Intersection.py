# Amazon: Given two arrays, write a function to get the intersection of the two. 
# For example, if A = [1, 2, 3, 4, 5] and B = [0, 1, 3, 7] then you should return [1, 3]

def intersection(arr1,arr2):
    res = [] # if repeated is there work with set
    for i in arr1:
        if i in arr2:
            res.append(i)
    return res

def intersection_one_line(arr1,arr2):
    return [x for x in arr1 if x in arr2]

A = [1, 2, 3, 4, 5] 
B = [0, 1, 3, 7]
print(intersection_one_line(A,B))
