# Akuna Capital: Given an integer array, find the sum of the largest contiguous subarray within the array.
# For example, if the input is [-1, -3, 5, 4, 3, -6, 9, 2], 
# then return 11 (because of [9, 2]). Note that if all the elements are negative, you should return 0.

# Best approach Kadens algo
def max_subarray_sum(nums):
    """
    Find maximum sum of contiguous subarray using Kadane's algorithm.
    Time: O(n), Space: O(1)
    """
    max_sum = float('-inf')
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum <= 0:
            curr_sum = 0
        else:
            max_sum = max(max_sum,curr_sum)
    return max_sum

# Test case
nums = [-1, -3, 5, -4, 3, -6, 9, 2]
print(max_subarray_sum(nums))  # Output: 11 (from [9, 2])
