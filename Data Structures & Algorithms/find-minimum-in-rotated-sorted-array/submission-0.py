class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find break point
        left=0 #jsut idx
        right=len(nums)-1

        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[right]:
                right=mid
            elif nums[right]<nums[mid]:
                left=mid+1


        return nums[left]
