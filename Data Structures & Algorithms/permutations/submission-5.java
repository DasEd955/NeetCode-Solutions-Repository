public class Solution {

    private List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> permute(int[] nums) {

        dfs(nums, 0);
        return result;
    }

    private void dfs(int[] nums, int index) {

        if(index == nums.length) {
            List<Integer> permutation = new ArrayList<>();
            for(int num : nums) {permutation.add(num);}
            result.add(permutation);
            return;
        }

        for(int i = index; i < nums.length; i++) {
            swap(nums, index, i);
            dfs(nums, index + 1);
            swap(nums, index, i);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}