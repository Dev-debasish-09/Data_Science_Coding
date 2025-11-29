class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = prices[0]
        max_profit = float('-inf')
        for i in range(len(prices)):
            first = min(first,prices[i])
            max_profit = max(max_profit,prices[i]-first)
        return max_profit
