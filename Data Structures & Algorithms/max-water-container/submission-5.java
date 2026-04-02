public class Solution {
    public int maxArea(int[] heights) {

        int left = 0;
        int right = heights.length - 1;
        int maxArea = 0;

        while(left < right) {
            int currentArea = (right - left) * Integer.min(heights[left], heights[right]);

            if(heights[left] < heights[right]) {
                left++;
                if(currentArea > maxArea) {
                    maxArea = currentArea;
                }
            }

            else {
                right--;
                if(currentArea > maxArea) {
                    maxArea = currentArea;
                }
            }
        }

        return maxArea;
    }

}
