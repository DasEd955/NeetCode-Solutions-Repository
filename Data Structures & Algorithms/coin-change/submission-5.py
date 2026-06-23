class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = dict()

        def backtrack(i: int, total: int) -> int:
            if i >= len(coins) or total > amount:
                return float("inf")
            if total == amount:
                return 0
            if (i, total) in cache:
                 return cache[(i, total)]
            take = 1 + backtrack(i, total + coins[i])
            skip = backtrack(i + 1, total)
            choice = min(take, skip)
            cache[(i, total)] = choice
            return choice
        
        result = backtrack(0, 0)
        return result if result != float("inf") else -1