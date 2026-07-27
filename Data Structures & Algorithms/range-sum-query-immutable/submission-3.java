class NumArray {

    private int[] prefix;

    public NumArray(int[] nums) {
        int[] prefix = new int[nums.length + 1];
        this.prefix = prefix;
        for(int i = 0; i < nums.length; i++) {
            this.prefix[i + 1] = this.prefix[i] + nums[i];
        }
    }
    
    public int sumRange(int left, int right) {  
        return this.prefix[right + 1] - this.prefix[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */