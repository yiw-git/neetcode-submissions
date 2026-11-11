class Solution:
    def threeSum(self, nums:List[int])->List[List[int]]:

        solutions=[]
        nums.sort()

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
        
            while left<right:
                if nums[left]+nums[i]+nums[right]>0:
                    right-=1
                elif nums[left]+nums[i]+nums[right]<0:
                    left+=1
                else:
                    solutions.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left-1]==nums[left]:
                        left+=1
                    while left<right and nums[right+1]==nums[right]:
                        right-=1

        return solutions

