class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l1=[0]*(len(nums)+1)
        l1[1]=nums[0]
        l1[2]=max(nums[0], nums[1])

        for i in range(3,len(nums)+1):
            l1[i]=max(nums[i-1]+l1[i-2],l1[i-1])
        return l1[-1]
