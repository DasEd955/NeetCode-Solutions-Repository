class Solution {
    public int maxArea(int[] heights) {

        int maxArea = 0, left = 0, right = heights.length - 1;

        while(left < right) {
            int currentArea = Integer.min(heights[left], heights[right]) * (right - left);
            maxArea = Integer.max(maxArea, currentArea);
            if(heights[left] <= heights[right]) {
                //maxArea = Integer.max(maxArea, currentArea);
                left++;
            }
            else {
                //maxArea = Integer.max(maxArea, currentArea);
                right--;
            }
        }
        return maxArea;
    }
}
