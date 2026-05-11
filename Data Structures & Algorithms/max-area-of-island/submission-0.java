class Solution {
    
    private static final int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    public int maxAreaOfIsland(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int maxArea = 0;

        for(int row = 0; row < rows; row++) {
            for(int col = 0; col < cols; col++) {
                if(grid[row][col] == 1) {
                    maxArea = Integer.max(maxArea, dfs(row, col, grid));
                }
            }
        }

        return maxArea;
    }

    private int dfs(int row, int col, int[][] grid) {
        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || grid[row][col] == 0) {return 0;}

        grid[row][col] = 0;
        int currentMax = 1;
        for(int[] dir : directions) {
            currentMax += dfs(row + dir[0], col + dir[1], grid);
        }

        return currentMax;
    }
}
