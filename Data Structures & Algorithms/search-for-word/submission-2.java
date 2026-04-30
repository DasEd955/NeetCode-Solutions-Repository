class Solution {
    public boolean exist(char[][] board, String word) {
        int rows = board.length, cols = board[0].length;
        
        for(int row = 0; row < rows; row++) {
            for(int col = 0; col < cols; col++) {
                if(dfs(row, col, 0, board, word) == true) {return true;}
            }
        }
        return false;
    }

    private boolean dfs(int row, int col, int index, char[][] board, String word) {
        if(index == word.length()) {return true;}
        int rows = board.length, cols = board[0].length;
        if(row < 0 || col < 0 || row >= rows || col >= cols) {return false;}
        if(board[row][col] != word.charAt(index)) {return false;}

        char temp = board[row][col];
        board[row][col] = '#';

        boolean left = dfs(row-1, col, index+1, board, word), right = dfs(row+1, col, index+1, board, word);
        boolean down = dfs(row, col-1, index+1, board, word), up = dfs(row, col+1, index+1, board, word);

        board[row][col] = temp;
        return left || right || up || down;
    }
}
