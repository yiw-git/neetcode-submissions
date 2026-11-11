from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count=defaultdict(int)
        for num in nums:
            count[num]+=1

        #count={4:12, 5:14, 6:17}
        #i do not know how sort them
        # Sort by value
#sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
        arr=[]
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res