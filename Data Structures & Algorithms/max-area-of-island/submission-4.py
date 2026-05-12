class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def bfs(row: int, col: int) -> int:
            queue = deque()
            visited.add((row, col))
            queue.append((row, col))
            currentMax = 1

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0 or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    currentMax += 1

            return currentMax
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea = max(maxArea, bfs(row, col))
        
        return maxArea
        