class Solution {
    public int largestRectangleArea(int[] heights) {

        class Pair {
            int index;
            int height;
            public Pair(int index, int height) {
                this.index = index;
                this.height = height;
            }
        }

        int maxArea = 0;
        Stack<Pair> stack = new Stack<>();

        for(int i = 0; i < heights.length; i++) {
            int startIndex = i;
            while(!stack.isEmpty() && stack.peek().height > heights[i]) {
                Pair popped = stack.pop();
                int index = popped.index, height = popped.height;
                maxArea = Integer.max(maxArea, height * (i - index));
                startIndex = index;
            }
            stack.push(new Pair(startIndex, heights[i]));
        }
        
        for(Pair pair : stack) {
            maxArea = Integer.max(maxArea, (heights.length - pair.index) * pair.height);
        }

        return maxArea;
    }
}
