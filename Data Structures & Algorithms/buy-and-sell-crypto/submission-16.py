class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        maxProfit = 0

        for i in range(len(prices)):
            buyPrice = prices[i]
            for j in range(i, len(prices)):
                sellPrice = prices[j]
                profit = sellPrice - buyPrice
                maxProfit = max(maxProfit, profit)

        return maxProfit               