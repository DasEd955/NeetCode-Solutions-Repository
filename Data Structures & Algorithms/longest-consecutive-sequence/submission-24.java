class Solution {
    public int longestConsecutive(int[] nums) {

        int longest = 0;
        HashSet<Integer> numsSet = new HashSet<>();

        for(int num : nums) {
            numsSet.add(num);
        }

        System.out.println(numsSet);

        for(int num : numsSet) {
            if(!numsSet.contains(num - 1)) {
                int length = 1;
                while(numsSet.contains(num + length)) {
                    length++;
                }
                longest = Integer.max(longest, length);
            }
        }
        return longest;
    }
}
