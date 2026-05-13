class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        minutes = 0
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2        
            minutes += (1 if queue else 0)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return minutes