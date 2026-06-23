class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = dict()

        def backtrack(i: int, total: int, numCoins: int) -> int:
            if i >= len(coins) or total > amount:
                return float("inf")
            if total == amount:
                return 0
            if (i, total) in memo:
                return memo[(i, total)]
            addSame = 1 + backtrack(i, total + coins[i], numCoins + 1)
            toNext = backtrack(i + 1, total, numCoins)
            choice = min(addSame, toNext)
            memo[(i, total)] = choice
            return choice
        
        result = backtrack(0, 0, 0)
        return result if result != float("inf") else -1