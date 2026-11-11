class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return [nums[1], nums[0]]
        
        prels=[]
        pre=1
        for i in range(0,len(nums)):
            if i==0:
                pre=1
            else:
                pre*=nums[i-1]
            prels.append(pre)
        endls=[]
        end=1
        print(prels)
        for j in range(len(nums)-1, -1,-1):
            if j==len(nums)-1:
                end=1
            else:
                end*=nums[j+1]
            endls.append(end)  
        print(endls)
        output=[]    
        for num in range(len(nums)):
            output.append(prels[num]*endls[len(nums)-1-num])
        return output










