class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        threeSum=[]
        
        for i in range(len(nums)-2):
            #two pointers
            if i>=1 and nums[i]==nums[i-1]:
                continue
            p1=i+1
            p2=len(nums)-1
            while p1<p2:
                total=nums[i]+nums[p1]+nums[p2]
                if total==0:
                    triple=[nums[i], nums[p1], nums[p2]]
                    threeSum.append(triple)
                    while p1<p2 and nums[p1]==nums[p1+1]:
                        p1+=1
                    while p1<p2 and nums[p2]==nums[p2-1]:
                        p2-=1
                    p1+=1
                    p2-=1
                elif total>0:
                    p2-=1
                else:
                    p1+=1
        return threeSum

