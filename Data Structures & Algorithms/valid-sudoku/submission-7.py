class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        #row 

        for i in range(9):
            l=board[i]
            seen=set()
            for num in l:
                if num !=".":
                    if num in seen:
                        return False
                    else:
                        seen.add(num)
        
        for j in range(9):
            seen=set()
            for i in range(9):
                num=board[i][j]
                if num !=".":
                    if num in seen:
                        return False
                    else:
                        seen.add(num)
        
        for i in [0,3,6]:
            for j in [0,3,6]:
                seen=set()
                for n in range(3):
                    for m in range(3):
                        num=board[i+n][j+m]
                        if num!=".":
                            if num in seen:
                                return False
                            else:
                                seen.add(num)
            print(seen)
        return True
            
                    

                    
            








