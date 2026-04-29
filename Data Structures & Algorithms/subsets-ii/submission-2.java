class Solution {

    private List<List<Integer>> result = new ArrayList<>();
    private List<Integer> subset = new ArrayList<>();

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        dfs(0, subset, nums);
        return result;
    }

    private void dfs(int index, List<Integer> subset, int[] nums) {
        result.add(new ArrayList<>(subset));

        for(int j = index; j < nums.length; j++) {
            if(j > index && nums[j] == nums[j - 1]) {continue;}
            subset.add(nums[j]);
            dfs(j + 1, subset, nums);
            subset.removeLast();
        }
    }
}
