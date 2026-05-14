class Pair {
    public int row, col;
    public Pair(int row, int col) {
        this.row = row;
        this.col = col;
    }
}

class Solution {

    private static final int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public void solve(char[][] board) {
        int rows = board.length, cols = board[0].length;

        bfs(board);
        for(int row = 0; row < rows; row++) {
            for(int col = 0; col < cols; col++) {
                if(board[row][col] == 'O') {
                    board[row][col] = 'X';
                }
                else if(board[row][col] == 'C') {
                    board[row][col] = 'O';
                }
            }
        }
    }

    private void bfs(char[][] board) {
        int rows = board.length, cols = board[0].length;
        Deque<Pair> queue = new ArrayDeque<>();
        for(int row = 0; row < rows; row++) {
            for(int col = 0; col < cols; col++) {
                if(board[row][col] == 'O' && (row == 0 || col == 0 || row == rows - 1 || col == cols - 1)) {
                    queue.offer(new Pair(row, col));
                }
            }
        }

        while(!queue.isEmpty()) {
            Pair popped = queue.removeFirst();
            int row = popped.row, col = popped.col;
            if(board[row][col] == 'O') {
                board[row][col] = 'C';
                for(int[] dir : directions) {
                    int nr = row + dir[0], nc = col + dir[1];
                    if(nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                        queue.offer(new Pair(nr, nc));
                    }
                }
            }
        }
    }
}
