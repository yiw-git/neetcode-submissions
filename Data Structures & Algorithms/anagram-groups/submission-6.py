class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l1=[]
        for word in strs:
            l1.append("".join(sorted(word)))
            #l1 = ["act","opts","opts","act","opts","aht"]
        d1={}
        #key: sorted word, value: list of idx
        for i in range(len(l1)):
            w=l1[i]
            if w in d1:
                d1[w].append(strs[i])
            else:
                d1[w]=[strs[i]]
     
        return list(d1.values())
           

