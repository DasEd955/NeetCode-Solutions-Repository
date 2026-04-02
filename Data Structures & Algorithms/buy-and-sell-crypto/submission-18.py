class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        maxProfit = 0
        left, right = 0, 1      # left=buyPrice, right=sellPrice          

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1

        return maxProfit               