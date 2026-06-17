class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = set()
        grids = set()
        grid_count = 0

        
        if len(board) == 0: 
            return False
        
        for r in range(len(board)):
            rows = set()
            for i in range(len(board[r])):
                if board[r][i] != ".":
                    # ROWS
                    if board[r][i] in rows:
                        return False
                    rows.add(board[r][i])

                    # COLUMN
                    if (board[r][i], i) in cols:
                        return False
                    cols.add((board[r][i], i))

                    # GRID
                    grid_id = (r // 3, i // 3)
                    if (board[r][i], grid_id) in grids:
                        return False
                    grids.add((board[r][i], grid_id))
                            
        return True