class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l1=[0]*len(nums)
        l1[0]=nums[0]
        l1[1]=max(nums[0], nums[1])

        for i in range(2,len(nums)):
            l1[i]=max(nums[i]+l1[i-2],l1[i-1])
        return l1[-1]
