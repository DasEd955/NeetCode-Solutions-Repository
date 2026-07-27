class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        int[] merged = intervals[0];
        int[][] result = new int[intervals.length][];
        int idx = 0;

        for (int i = 1; i < intervals.length; i++) {
            if (merged[1] >= intervals[i][0]) {
                merged[0] = Math.min(merged[0], intervals[i][0]);
                merged[1] = Math.max(merged[1], intervals[i][1]);
            } else {
                result[idx++] = merged;
                merged = intervals[i];
            }
        }

        result[idx++] = merged;

        return Arrays.copyOf(result, idx);
    }
}