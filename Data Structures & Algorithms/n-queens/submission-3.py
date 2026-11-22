class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.']*n for i in range(n)]

        def backtracking(r):
            #first check if it is the bottom
            if r==n:#now we have found the valid path
                str_row=[''.join(row) for row in board]
                res.append(str_row)
                return
            for c in range(n):
                if self.isvalid(r,c,board):
                    board[r][c]='Q'
                    backtracking(r+1)
                    board[r][c]='.'
                    
        backtracking(0)
        return res

    def isvalid(self,r,c,board):
        row=r-1
        while row>=0:
            if board[row][c]=='Q':
                return False
            row-=1
        
        row,col=r-1,c-1
        while row>=0 and col>=0:
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
        
        row,col=r-1,c+1
        while row>=0 and col<len(board):
            if board[row][col]=='Q':
                return False
            row-=1
            col+=1
        return True


