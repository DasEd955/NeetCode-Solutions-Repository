class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            middle = left + (right - left) // 2
            row, col = middle // cols, middle % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False
        