# Google: 
# Say you have an n-by-n matrix of elements that are sorted in ascending order both in the columns and rows of the matrix. 
# Return the k-th smallest element of the matrix. For example, consider the matrix below:
# [[1 4 7]  [3 5 9]  [6 8 11]]
# if K = 4 then return 5


def kth_smallest_in_sorted_matrix(matrix, k):
    """
    Simple approach: flatten matrix and sort.
    Time: O(n² log n²), Space: O(n²)
    """
    if not matrix or not matrix[0]:
        return None
    
    # Flatten matrix and sort
    flattened = []
    for row in matrix:
        flattened.extend(row)
    
    flattened.sort()
    return flattened[k-1] if k <= len(flattened) else None

# Test case
matrix = [
    [1, 4, 7],
    [3, 5, 9],
    [6, 8, 11]
]
print(kth_smallest_in_sorted_matrix(matrix, 1))  # Output: 1
print(kth_smallest_in_sorted_matrix(matrix, 4))  # Output: 5
