"""
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


class Solution:
    def topKFrequent(self, nums:List[int], k:int)->List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]

        for num in nums:
            count[num]= 1 + count.get(num,0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res=[]
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
"""
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums:List[int], k:int)->List[int]:
        count=defaultdict(int)
        freq=[[] for i in range(len(nums)+1)]
        for num in nums:
            count[num]+=1
        
        for num, cnt in count.items():
            freq[cnt].append(num)

        """
        freq=[
        0[],
        1[],
        2[number 3, number 6],
        3[number 1, number 11],
        4[],
        5[number 4],
        ]

        """
        #for exmple, k=3 top three 

        output=[]
        top=0
        for i in range(len(freq)-1,0,-1):
            
            if len(freq[i])>0 and top<k:
                for num in freq[i]:
                    output.append(num)
                    top+=1

        return output
        """
        freq=[
        [],
        [1],
        [2],
        [3],
        [],
        [],
        []        ]
        
        """




