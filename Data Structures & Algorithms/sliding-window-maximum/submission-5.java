class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        
        int[] result = new int[nums.length - k + 1];
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        int left = 0, right = 0;

        while(right < nums.length) {
            while(!queue.isEmpty() && nums[queue.getLast()] < nums[right]) {
                queue.pollLast();
            }
            queue.add(right);
            if(left > queue.getFirst()) {
                queue.pollFirst();
            }
            if(right + 1 >= k) {
                result[left] = nums[queue.getFirst()];
                left++;
            }
            right++;
        }
        return result;

    }
}
