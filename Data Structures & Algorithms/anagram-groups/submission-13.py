class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #cat, and tax, use hash map, On, On,
        #{'c':1; 'a':1, 't':1}can i use the dict as the key for another dict??
        #more element
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())

