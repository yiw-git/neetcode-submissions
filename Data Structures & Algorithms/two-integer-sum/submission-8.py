class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic1={}

        for idx, val in enumerate(nums):
            diff=target-val
            if diff in dic1:
                return [dic1[diff], idx]
            dic1[val]=idx