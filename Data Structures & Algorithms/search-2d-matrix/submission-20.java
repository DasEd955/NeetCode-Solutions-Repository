class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        int rows = matrix.length, cols = matrix[0].length;
        int left = 0, right = rows * cols - 1;

        while(left <= right) {
            int middle = left + (right - left) / 2;
            int row = Math.floorDiv(middle, cols), col = middle % cols;
            if(matrix[row][col] == target) {
                return true;
            }
            else if(matrix[row][col] < target) {
                left = middle + 1;
            }
            else {
                right = middle - 1;
            }
        }
        return false;

    }
}
