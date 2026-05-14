class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(board), len(board[0])

        def bfs() -> None:
            queue = deque()
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == 'O' and (row == 0 or col == 0 or row == rows - 1 or col == cols - 1):
                        queue.append((row, col))
            
            while queue:
                row, col = queue.popleft()
                if board[row][col] == 'O':
                    board[row][col] = 'C'
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            queue.append((nr, nc))
            
        bfs()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'C':
                    board[row][col] = 'O'