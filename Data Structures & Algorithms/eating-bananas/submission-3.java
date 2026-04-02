class Solution {

    public int calcMax(int[] piles) {
        int currentMax = 0;
        for(int pile: piles) {
            currentMax = Integer.max(currentMax, pile);
        }
        return currentMax;
    }

    public int minEatingSpeed(int[] piles, int h) {

        int left = 1, right = calcMax(piles);

        while(left <= right) {
            int middle = left + (right - left) / 2, totalHours = 0;
            for(int pile : piles) {
                totalHours += (pile + middle - 1) / middle;
            }
            if(totalHours <= h) {
                right = middle - 1;
            }
            else {
                left = middle + 1;
            }
        }
        return left;
    }
}
