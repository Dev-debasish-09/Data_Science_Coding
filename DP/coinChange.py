class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = {}

        def dfs(i,amt):
            if amt == 0:
                return 0
            if i == n or amt<0 :
                return float('inf')
            if (i,amt) in dp:
                return dp[(i,amt)]
            not_take = dfs(i+1,amt)
            take = 1+dfs(i,amt - coins[i])

            dp[(i,amt)] = min(take,not_take)
            return dp[(i,amt)]

        ans = dfs(0,amount)
        return ans if ans != float('inf') else -1
