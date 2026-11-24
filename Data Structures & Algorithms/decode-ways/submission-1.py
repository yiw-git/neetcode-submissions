class Solution:
    def numDecodings(self, s: str) -> int:

        def helper(substr):
            if not substr or substr[0]=='0':
                return False
            return 1<=int(substr)<=26
            
        nums=[0]*(len(s)+1)
        nums[0]=1
        for i in range(1,len(s)+1):

            if i>=2 and helper(s[i-2:i]):
                nums[i]+=nums[i-2]
            if helper(s[i-1:i]):
                nums[i]+=nums[i-1]
           
        return nums[len(s)]
                
