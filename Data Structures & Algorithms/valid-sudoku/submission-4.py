from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #1 Declere my hasg sets
        row     = defaultdict(set)
        col     = defaultdict(set)
        subBox  = defaultdict(set)

        #2 iterate throught my board
        for r in range(len(board)):
            for c in range(len(board[r])):
                #2.1 Avoid compute '.'
                if board[r][c] == '.': continue

                #2.2 Faild conditions
                if (board[r][c] in row[r] or 
                    board[r][c] in col[c] or 
                    board[r][c] in subBox[(r // 3, c // 3)] ):
                    return False
                
                #2.3 Adding value to the respective HashSet
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                subBox[(r // 3, c // 3)].add(board[r][c])
                print(f'row: {row}')
                print(f'col {col}')
                print(f'subBox: {subBox}')


        return True
