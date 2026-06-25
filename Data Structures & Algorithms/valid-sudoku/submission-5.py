class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = defaultdict(set)
        group = defaultdict(set)

        for i in range(len(board)):
            row = set()
            for j in range(len(board[i])):
                group_id = (i // 3, j // 3)
                
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in row
                or board[i][j] in col[j] 
                or board[i][j] in group[group_id]):
                    return False
    
                row.add(board[i][j])
                col[j].add(board[i][j])
                group[group_id].add(board[i][j])
                     
        return True