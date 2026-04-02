public class Solution {
    public int longestConsecutive(int[] nums) {
        
        if(nums.length == 0) {return 0;}

        HashSet<Integer> numsSet = new HashSet<>();
        for(Integer num : nums) {numsSet.add(num);}
        int longestSeq = 0;

        for(Integer num : numsSet) {

            if(!(numsSet.contains(num - 1))) {
                int length = 0;
                while(numsSet.contains(num + length)) {
                    length++;
                }
                longestSeq = Integer.max(length, longestSeq);
            }
        }
        return longestSeq;
    }
}
