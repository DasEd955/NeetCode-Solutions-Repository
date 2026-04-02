class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if not board:
            return False

        for row in board:
            row  = [x for x in row if x != '.']
            seenRow = set(row)
            if len(row) != len(seenRow):
                return False

        for i in range(len(board)):
            column = [board[j][i] for j in range(len(board)) if board[j][i] != '.']
            seenCol = set(column)
            if len(column) != len(seenCol):
                return False

        for squareRow in range(0, 9, 3):
            for squareCol in range(0, 9, 3):
                seenSquares = set()
                for i in range(3):
                    for j in range(3):
                        value = board[squareRow + i][squareCol + j]
                        if value == '.':
                            continue
                        if value in seenSquares:
                            return False
                        seenSquares.add(value)    

        return True                                            
        