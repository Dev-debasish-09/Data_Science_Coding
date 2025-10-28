# AQR: Given two lists X and Y, return their correlation

import math
def find_corr(arr1,arr2):
    n = len(arr1)

    if n != len(arr2) or n == 0:
        return None
    
    mean_x = sum(arr1)/len(arr1)
    mean_y = sum(arr2)/len(arr2)

    cov = 0
    var_x = 0
    var_y = 0

    for i in range(n):
        diff_x = arr1[i] - mean_x
        diff_y = arr2[i] - mean_y

        var_x += diff_x**2
        var_y += diff_y**2
        cov += diff_y*diff_x

    if var_x == 0 or var_y == 0:
        return 0
    
    corr = cov/math.sqrt(var_x*var_y)

    return corr

X = [1, 2, 3, 4, 5]
Y = [4, 3, 2, 7, 10]

print(find_corr(X,Y))
