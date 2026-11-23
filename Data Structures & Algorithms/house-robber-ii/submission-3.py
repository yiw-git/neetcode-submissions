class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l1=nums[1:] #no first
        l2=nums[:-1]

        def dfs(nums)->int:
            if len(nums)==1:
                return nums[0]
            l3=[0]*len(nums)
            l3[0]=nums[0]
            l3[1]=max(nums[0], nums[1])
            for i in range(2, len(nums)):
                l3[i]=max(nums[i]+l3[i-2], l3[i-1])
            return l3[-1]

        return max(dfs(l1), dfs(l2))
'''
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
#time space complexity is O(n)
'''