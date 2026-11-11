
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1={}
        #key: element, value: frequency
        for num in nums:
            d1[num]=d1.get(num,0)+1

        l1=[]
        for key,v in d1.items():
            l1.append((key,v))
        l1.sort(key=lambda x:x[1], reverse=True)

        res=[]
        for i in range(k):
            res.append(l1[i][0])
        return res
