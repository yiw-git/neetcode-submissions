"""class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in nums:
            b=target-a
            if b in nums:
                idxb=nums.index(b)# how to ifnd b index in list nums 
                idxa=nums.index(a)
        return [idxa, idxb]"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for idx, num in enumerate(nums):
            b=target-num

            if b in seen:
                return [seen[b],idx]
            seen[num]=idx