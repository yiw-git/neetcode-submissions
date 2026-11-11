class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            mid_num=nums[mid]
            if mid_num<target:
                l=mid+1
            elif mid_num>target:
                r=mid-1
            else:
                return mid
        if l==r:
            if target>nums[r]:
                return r+1
            if target<nums[l]:
                return 0
        else:
            return l