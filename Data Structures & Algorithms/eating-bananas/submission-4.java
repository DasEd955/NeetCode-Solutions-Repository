class Solution {

    public int max(int[] piles) {
        int max = 0;
        for(int pile: piles) {
            max = Integer.max(max, pile);
        }
        return max;
    }

    public int minEatingSpeed(int[] piles, int h) {
        
        int low = 1, high = max(piles);

        while(low <= high) {
            int middle = low + (high - low) / 2, totalHours = 0;
            for(int pile : piles) {
                totalHours += (pile + middle - 1) / middle;
            }
            if(totalHours <= h) {
                high = middle - 1;
            }
            else {
                low = middle + 1;
            }
        }
        return low;
    }
}
