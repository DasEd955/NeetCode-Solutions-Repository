class Solution {

    private List<List<String>> result = new ArrayList<>();
    private Set<Integer> cols = new HashSet<>(), diag1 = new HashSet<>(), diag2 = new HashSet<>();

    public List<List<String>> solveNQueens(int n) {
        char[][] board = new char[n][n];
        for(char[] row : board) {Arrays.fill(row, '.');}

        dfs(0, n, board);
        return result;
    }

    private void dfs(int row, int n, char[][] board) {
        if(row == n) {
            List<String> copy = new ArrayList<>();
            for(char[] r : board) {
                copy.add(new String(r));
            }
            result.add(copy);
            return;
        }

        for(int col = 0; col < n; col++) {
            if(cols.contains(col) || diag1.contains(row - col) || diag2.contains(row + col)) {continue;}          

            board[row][col] = 'Q';
            cols.add(col);
            diag1.add(row - col);
            diag2.add(row + col);

            dfs(row + 1, n, board);

            board[row][col] = '.';
            cols.remove(col);
            diag1.remove(row - col);
            diag2.remove(row + col);
        }
    }
}
