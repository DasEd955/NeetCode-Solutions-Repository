class Solution {

    private static final int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        int rows = heights.length, cols = heights[0].length;
        boolean[][] atlantic = new boolean[rows][cols], pacific = new boolean[rows][cols];

        for(int row = 0; row < rows; row++) {
            dfs(row, 0, pacific, heights[row][0], heights);
            dfs(row, cols - 1, atlantic, heights[row][cols - 1], heights);
        }

        for(int col = 0; col < cols; col++) {
            dfs(0, col, pacific, heights[0][col], heights);
            dfs(rows - 1, col, atlantic, heights[rows - 1][col], heights);
        }

        for(int row = 0; row < rows; row++) {
            for(int col = 0; col < cols; col++) {
                if(atlantic[row][col] && pacific[row][col]) {
                    result.add(Arrays.asList(row, col));
                }
            }
        }

        return result;
    }

    private void dfs(int row, int col, boolean[][] visited, int prevHeight, int[][] heights) {
        int rows = heights.length, cols = heights[0].length;
        if(row < 0 || col < 0 || row >= rows || col >= cols || 
           visited[row][col] || heights[row][col] < prevHeight) {return;}

        visited[row][col] = true;
        
        for(int[] dir : directions) {
            int nr = row + dir[0], nc = col + dir[1];
            dfs(nr, nc, visited, heights[row][col], heights);
        }
    }
}
