class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0

        for i in range(len(prices)):
            buyDay = prices[i]
            for j in range(i, len(prices)):
                profit = prices[j] - buyDay
                maxProfit = max(maxProfit, profit)

        return maxProfit        
