# P - N = target
# P + N = total
# 2P = target + total
# P = (target + total) / 2

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        for num in nums:
            next_dp = {}

        # For each sum already possible, add and subtract current num
            for s, count in dp.items():

                # Add operation
                new_sum_add = s + num
                next_dp[new_sum_add] = next_dp.get(new_sum_add, 0) + count

                # Subtract operation
                new_sum_sub = s - num
                next_dp[new_sum_sub] = next_dp.get(new_sum_sub, 0) + count

            dp = next_dp  # move to next iteration

        return dp.get(target, 0)




         
