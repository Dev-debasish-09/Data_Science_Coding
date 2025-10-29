class Solution:
    def maxArea(self, height: List[int]) -> int:
       first = 0
       last = len(height) - 1
       res = float('-inf')
       curr_sum = 0
       while first < last:
        l = min(height[first],height[last])
        b = last - first
        curr_sum = l*b
        res = max(res,curr_sum)
        if height[first] < height[last]:
            first += 1
        else:
            last -= 1
       return res

