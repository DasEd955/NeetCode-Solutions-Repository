class Solution {
    public boolean isValidSudoku(char[][] board) {

        Map<Integer, Set<Character>> rows = new HashMap<>(); 
        Map<Integer, Set<Character>> cols = new HashMap<>();   
        Map<Integer, Set<Character>> squares = new HashMap<>(); 

        for(int row = 0; row < 9; row++) {
            for(int col = 0; col < 9; col++) {
                if(board[row][col] == '.') {
                    continue;
                }

                int squareIndex = (row / 3) * 3 + (col / 3);

                rows.putIfAbsent(row, new HashSet<>());
                cols.putIfAbsent(col, new HashSet<>());
                squares.putIfAbsent(squareIndex, new HashSet<>());

                if(rows.get(row).contains(board[row][col]) ||
                   cols.get(col).contains(board[row][col]) || 
                   squares.get(squareIndex).contains(board[row][col])) {
                    return false;
                }
                
                rows.get(row).add(board[row][col]);
                cols.get(col).add(board[row][col]);
                squares.get(squareIndex).add(board[row][col]);
            }
        }

        return true;
        
    }
}
