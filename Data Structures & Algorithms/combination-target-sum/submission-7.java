class Solution {
    
    private List<List<Integer>> result = new ArrayList<>();
    private List<Integer> combo = new ArrayList<>();
    
    public List<List<Integer>> combinationSum(int[] nums, int target) {

        Arrays.sort(nums);
        
        dfs(0, nums, combo, target, 0);
        return result;
    }

    private void dfs(int index, int[] nums, List<Integer> combo, int target, int currSum) {

        if(currSum == target) {
            result.add(new ArrayList<>(combo));
            return;
        }

        for(int j = index; j < nums.length; j++) {
            if(currSum + nums[j] > target) {return;}
            combo.add(nums[j]);
            dfs(j, nums, combo, target, currSum + nums[j]);
            combo.removeLast();
        }
    }
}
