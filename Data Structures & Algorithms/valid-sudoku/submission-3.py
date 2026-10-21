class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsC = dict()
        columsC = dict()
        subBoxC = dict()
        # TODO #1: Check rows rule
        for r in board:
            for c in r:
                if c == ".": continue
                if rowsC.get(c, 0) != 0: return False
                rowsC[c] =  rowsC.get(c, 1)
            rowsC = dict()

        # TODO #2: Check Colums rule
        for c in range(len(board[0])):
            for r in range(len(board)):
                if board[r][c] == ".": continue
                if columsC.get(board[r][c], 0) != 0: return False
                columsC[board[r][c]] =  columsC.get(board[r][c], 1)
            columsC = dict()
        
        # TODO #3: Check each o one sub-boxes
        ih = 0
        iv = 0
        h = 3
        v = 3
        for subBox in range(1,10):

            print(f'(SUBBOX: {subBox})  ih: {ih}, iv: {iv}, h: {h}, v: {v}')

            for r in range(iv, v):
                for c in range(ih, h):
                    print(f'i: {subBoxC}')
                    print(f'{r} : {c}')
                    if board[r][c] == ".": continue
                    if subBoxC.get(board[r][c], 0) != 0: return False
                    subBoxC[board[r][c]] = subBoxC.get(board[r][c], 1)
                    print(f'o: {subBoxC}')

            subBoxC = dict()


            if subBox % 3 == 0:
                ih = 0
                h = 3
                iv = v
                v += 3
                
            else:
                ih = h
                h += 3

            #print(f'(SUBBOX: {subBox}) ih: {ih}, iv: {iv}, h: {h}, v: {v}')


                
            

        return True