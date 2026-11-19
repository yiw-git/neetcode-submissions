class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        count=0

        def dfs(r,c):
            #out of bound
            if r<0 or c<0 or r>=ROWS or c>=COLS:
                return
            #value does not meet
            if grid[r][c]=='0':
                return
            grid[r][c]='0'
            direct=[(0,1),(0,-1),(1,0),(-1,0)]
            for dr, dc in direct:
                dfs(r+dr, c+dc)
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1':
                    dfs(r,c)
                    count+=1
        return count