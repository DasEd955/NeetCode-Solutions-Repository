class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
        int max = piles[0];
        for(int pile : piles) {
            if(pile > max) {
                max = pile;
            }
        }

        int low = 1, high = max;

        while(low <= high) {
            int middle = low + (high - low) / 2;
            int totalHours = 0;
            for(int pile : piles) {
                totalHours += Math.ceilDiv(pile, middle);
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
