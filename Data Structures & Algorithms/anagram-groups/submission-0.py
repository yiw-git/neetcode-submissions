"""class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)<=1:
            return [strs]
        
    
    out1=set()
    for astr in strs:


    def isAnagram(self, str1:str, str2:str)-> bool:
        if len(str1)!=len(str2):
            return False
        count={}
        for i in str1:
            count[i]=count.get(i,0)+1
        
        for j in str2:
            if j not in count:
                return False
            count[j]-=1
            if count[j]==0:
                del count[j]
        return len(count)==0
"""
class Solution:
    def groupAnagrams(self, strs:List[str])->List[List[str]]:
        res=defaultdict(list)
        for s in strs: #for every str, create the 26 list
            count=[0]*26
            for c in s: # for every ch in str, find index 
                count[ord(c)-ord('a')]+=1 #their relative index, dict value +1
            res[tuple(count)].append(s)
        return list(res.values())





