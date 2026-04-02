class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            row = matrix[i]
            left, right = 0, len(row) - 1
            while left <= right:
                middle = left + (right - left) // 2
                if row[middle] == target:
                    return True
                elif row[middle]< target:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return False
        