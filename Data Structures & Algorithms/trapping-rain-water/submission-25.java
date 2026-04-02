class Solution {
    public int trap(int[] height) {

        int maxArea = 0, left = 0, right = height.length - 1;
        int maxLeft = 0, maxRight = 0;

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
