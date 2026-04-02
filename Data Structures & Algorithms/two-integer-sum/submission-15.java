class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> seenDiffs = new HashMap<>();
        int[] pair = new int[2];

        for(int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if(seenDiffs.containsKey(diff)) {
                pair[0] = seenDiffs.get(diff);
                pair[1] = i;
            }
            else {
                seenDiffs.put(nums[i], i);
            }
        }
        return pair;
    }
}
