class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = dict()
        
        def backtrack(amount: int) -> int:
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            result = float("inf")
            for coin in coins: 
                if amount - coin >= 0:
                    result = min(result, 1 + backtrack(amount - coin))
            memo[amount] = result
            return result
        
        minCoins = backtrack(amount)
        return minCoins if minCoins != float("inf") else -1 