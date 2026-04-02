class Bar {

    public int index;
    public int height;

    public Bar(int index, int height) {
        this.index = index;
        this.height = height;
    }
}

class Solution {
    public int largestRectangleArea(int[] heights) {

        int maxArea = 0;
        Stack<Bar> stack = new Stack<>();

        for(int i = 0; i < heights.length; i++) {
            int startIndex = i;
            while(!stack.isEmpty() && stack.peek().height > heights[i]) {
                Bar poppedItem = stack.pop();
                int index = poppedItem.index, height = poppedItem.height;
                maxArea = Integer.max(maxArea, height * (i-index));
                startIndex = index;
            }
            stack.push(new Bar(startIndex, heights[i]));
        }

        for(Bar bar : stack) {
            maxArea = Integer.max(maxArea, bar.height * (heights.length - bar.index));
        }

        return maxArea;
    }
}
