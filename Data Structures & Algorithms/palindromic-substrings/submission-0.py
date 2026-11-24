class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        def expand(left, right):#find the al the valid substrings centered with 
            count=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            return count
        total_num=0
        for i in range(len(s)):
            total_num+=expand(i,i)
            total_num+=expand(i,i+1)
        return total_num


            


        
