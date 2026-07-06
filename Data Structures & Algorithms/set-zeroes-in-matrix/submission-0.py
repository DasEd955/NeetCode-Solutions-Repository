class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        seenZeros = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    seenZeros.add((r, c))
        
        rows, cols = len(matrix), len(matrix[0])
        for row, col in seenZeros:
            for r in range(rows):
                matrix[r][col] = 0
            for c in range(cols):
                matrix[row][c] = 0
        
        