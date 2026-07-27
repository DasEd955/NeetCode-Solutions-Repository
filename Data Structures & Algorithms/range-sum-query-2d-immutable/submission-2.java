class NumMatrix {

    private int[][] prefix;

    public NumMatrix(int[][] matrix) {
        int rows = matrix.length, cols = matrix[0].length;
        int[][] prefix = new int[rows + 1][cols + 1];
        this.prefix = prefix;

        for(int r = 0; r < rows; r++) {
            for(int c = 0; c < cols; c++) {
                this.prefix[r + 1][c + 1] = (
                    matrix[r][c]
                    + this.prefix[r][c + 1]
                    + this.prefix[r + 1][c]
                    - this.prefix[r][c]
                );
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return (
            this.prefix[row2 + 1][col2 + 1]
            - this.prefix[row1][col2 + 1]
            - this.prefix[row2 + 1][col1]
            + this.prefix[row1][col1]
        );
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */