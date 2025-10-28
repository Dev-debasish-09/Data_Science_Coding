# D.E. Shaw: Given an integer array, return the maximum product of any three numbers in the array. 
# For example, for A = [1, 3, 4, 5] you should return 60, while for B = [- 2, - 4, 5, 3] you should return 40.

def max_three_prod(arr):
    """
    Find maximum product of three numbers using sorting.
    Time: O(n log n), Space: O(1)
    """
    arr.sort()
    n = len(arr)
    # Maximum product can be either:
    # 1. Three largest numbers (all positive or all negative)
    # 2. Two smallest (negative) numbers * largest number
    return max(arr[n-1]*arr[n-2]*arr[n-3],arr[n-1]*arr[0]*arr[1])

#Brute Force
def max_three_prod_bf(arr):
     """
        Brute force approach - check all triplets.
        Time: O(n^3), Space: O(1)
     """
     n = len(arr)
     max_prod = float('-inf')

     for i in range(n):
          for j in range(i+1,n):
               for k in range(j+1,n):
                    product = arr[i]*arr[j]*arr[k]
                    if product > max_prod:
                         max_prod = product

     return max_prod



A = [1, 3, 4, 5]
B = [- 2, - 4, 5, 3]
print(max_three_prod_bf(A))
print(max_three_prod_bf(B))
