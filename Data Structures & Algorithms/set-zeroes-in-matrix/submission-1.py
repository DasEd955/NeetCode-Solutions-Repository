class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        seenZeros = set()
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    seenZeros.add((r, c))

        for row, col in seenZeros:
            for r in range(rows):
                matrix[r][col] = 0
            for c in range(cols):
                matrix[row][c] = 0
        
        