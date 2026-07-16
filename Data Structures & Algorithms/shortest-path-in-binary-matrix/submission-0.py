class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        rows, cols = len(grid), len(grid[0])   
        queue = deque([(0, 0, 1)])
        visited = set()
        visited.add((0, 0))

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1

        while queue:
            row, col, steps = queue.popleft()
            if row == rows - 1 and col == cols - 1:
                return steps
            visited.add((row, col))
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    queue.append((nr, nc, steps + 1))
                    visited.add((nr, nc))
        
        return -1