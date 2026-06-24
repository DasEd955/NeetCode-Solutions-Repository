class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        result = float("inf")
        for x in range(amount + 1):
            for coin in coins:
                if x - coin >= 0:
                    dp[x] = min(dp[x], 1 + dp[x - coin])
        
        return dp[-1] if dp[-1] != float("inf") else -1