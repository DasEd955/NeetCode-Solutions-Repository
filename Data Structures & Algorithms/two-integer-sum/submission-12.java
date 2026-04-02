class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seenDiffs = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if(seenDiffs.containsKey(diff)) {
                return new int[] {seenDiffs.get(diff), i};
            }
            else {
                seenDiffs.put(nums[i], i);
            }
        }
        return new int[] {};
    }
}
