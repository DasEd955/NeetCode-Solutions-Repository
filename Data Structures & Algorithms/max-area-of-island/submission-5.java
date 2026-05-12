class Pair {
    public int row, col;
    public Pair(int row, int col) {
        this.row = row;
        this.col = col;
    }
}

class Solution {
    
    private static final int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    public int maxAreaOfIsland(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int maxArea = 0;

        for(int row = 0; row < rows; row++) {
            for(int col = 0; col < cols; col++) {
                if(grid[row][col] == 1) {
                    maxArea = Integer.max(maxArea, bfs(row, col, grid));
                }
            }
        }

        return maxArea;
    }

    private int bfs(int row, int col, int[][] grid) {
        Deque<Pair> queue = new ArrayDeque<>();
        grid[row][col] = 0;
        queue.offer(new Pair(row, col));
        int currentMax = 1;

        while(!queue.isEmpty()) {
            Pair popped = queue.removeFirst();
            int r = popped.row, c = popped.col;
            for(int[] dir : directions) {
                int nr = r + dir[0], nc = c + dir[1];
                if(nr < 0 || nc < 0 || nr >= grid.length || nc >= grid[0].length || grid[nr][nc] == 0) {continue;}
                grid[nr][nc] = 0;
                queue.offer(new Pair(nr, nc));
                currentMax++;
            }
        }

        return currentMax;
    }
}
