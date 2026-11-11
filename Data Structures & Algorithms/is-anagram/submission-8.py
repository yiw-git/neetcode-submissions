class Solution:
    def isAnagram(self, s:str, t:str)-> bool:
        if len(s)!=len(t):
            return False
        count={}
        for a in s:
            count[a]=count.get(a,0)+1
        
        for b in t:
            if b not in count:
                return False
            count[b]-=1
            if count[b]==0:
                del count[b]
        return len(count)==0



