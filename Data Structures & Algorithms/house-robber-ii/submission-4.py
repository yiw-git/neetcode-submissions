class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        l1=nums[1:]
        l2=nums[:-1]
        def rob_line(nums):
            prev2,prev1=0,0
            for num in nums:
                cur=max(prev2+num, prev1)
                prev2=prev1
                prev1=cur
            return prev1
        return max(rob_line(l1), rob_line(l2))

