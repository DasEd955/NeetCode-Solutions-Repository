class Solution {
    public int trap(int[] height) {
        
        int maxArea = 0;
        int left = 0;
        int right = height.length - 1;
        int maxLeft = 0;
        int maxRight = 0;

        while(left < right) {

            if(height[left] <= height[right]) {
                maxLeft = Integer.max(maxLeft, height[left]);
                maxArea += maxLeft - height[left];
                left++;
            }
            else {
                maxRight = Integer.max(maxRight, height[right]);
                maxArea += maxRight - height[right];
                right--;
            }
        }
        return maxArea;
    }
}
