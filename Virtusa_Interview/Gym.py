class UserMainCode(object):
    @classmethod
    def minWorkoutMinutes(cls, input1, input2, input3):
        N = input1
        K = input2
        T = input3
        
        # dp[i] = min workout for first i days where day i is a workout day
        dp = [float('inf')] * (N + 1)
        
        # We can start by working out on any of the first K+1 days
        for i in range(1, min(K+2, N+1)):
            dp[i] = T[i-1]
        
        for i in range(1, N + 1):
            if dp[i] == float('inf'):
                continue
                
            # From day i, we can skip 0 to K days and then workout
            for skip in range(0, K+1):
                next_day = i + skip + 1
                if next_day <= N:
                    dp[next_day] = min(dp[next_day], dp[i] + T[next_day-1])
        
        # Answer is the minimum among the last K+1 positions
        result = float('inf')
        for i in range(max(1, N-K), N+1):
            result = min(result, dp[i])
        
        return result
