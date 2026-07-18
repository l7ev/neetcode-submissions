class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_col = collections.defaultdict(set)
        seen_row = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = (r/3, c/3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in seen_row[r] or 
                    board[r][c] in seen_col[c] or
                    board[r][c] in squares[(r //3, c // 3)]):
                    return False

                seen_row[r].add(board[r][c])
                seen_col[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True