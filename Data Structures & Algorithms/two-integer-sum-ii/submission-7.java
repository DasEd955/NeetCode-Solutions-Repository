class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int left = 0, right = numbers.length - 1;
        int[] result = new int[2];

        while(left < right) {
            int currentSum = numbers[left] + numbers[right];
            if(currentSum > target) {
                right--;
            }
            else if(currentSum < target) {
                left++;
            }
            else{
                result[0] = left + 1;
                result[1] = right + 1;
                left++;
                right--;
            }
        }
        return result;
    }
}
