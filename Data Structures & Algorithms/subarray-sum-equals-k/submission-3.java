class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> prefixSums = new HashMap<>();
        prefixSums.put(0, 1);
        int currentPrefix = 0, result = 0;

        for(int num : nums) {
            currentPrefix += num;
            int needed = currentPrefix - k;
            result += prefixSums.getOrDefault(needed, 0);
            prefixSums.put(currentPrefix, 1 + prefixSums.getOrDefault(currentPrefix, 0));
        }

        return result;
    }
}