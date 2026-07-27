class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();

        for(int i = 0; i < intervals.length; i++) {
            int[] interval = intervals[i];

            if(interval[1] < newInterval[0]) {
                result.add(interval);
            }
            else if(newInterval[1] < interval[0]) {
                result.add(newInterval);
                while(i < intervals.length) {
                    result.add(intervals[i]);
                    i++;
                }
                return result.toArray(new int[result.size()][]);
            }
            else {
                newInterval[0] = Math.min(newInterval[0], interval[0]);
                newInterval[1] = Math.max(newInterval[1], interval[1]);
            }
        }

        result.add(newInterval);
        return result.toArray(new int[result.size()][]);
    }
}
