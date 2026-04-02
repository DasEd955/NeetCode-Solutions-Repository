class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        HashMap<Integer, Integer> count = new HashMap<>();
        ArrayList<ArrayList<Integer>> frequency = new ArrayList<>();
        int[] result = new int[k];
        
        for(int i = 0; i < nums.length; i++) {
            count.put(nums[i], count.getOrDefault(nums[i], 0) + 1);
        }

        for(int i = 0; i <= nums.length; i++) {
            frequency.add(new ArrayList<>());
        }

        for(Map.Entry<Integer, Integer> entry : count.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();
            frequency.get(freq).add(num);
        }

        int index = 0;
        for(int i = frequency.size() - 1; i >= 0; i--) {
            for(int j = 0; j < frequency.get(i).size(); j++) {
                result[index++] = frequency.get(i).get(j);
                if(index == k) {
                    return result;
                }
            }
        }
        return result;
    }
}
