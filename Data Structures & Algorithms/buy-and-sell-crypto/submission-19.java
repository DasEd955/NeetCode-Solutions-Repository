class Solution {
    public int maxProfit(int[] prices) {

        int left = 0, right = 1, maxProfit = 0;

        while(right < prices.length) {
            if(prices[right] > prices[left]) {
                int profit = prices[right] - prices[left];
                maxProfit = Integer.max(profit, maxProfit);
            }
            else {
                left = right;
            }
            right++;
        }
        return maxProfit;
    }
}
