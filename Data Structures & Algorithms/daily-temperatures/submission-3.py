class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n 

        stack=[]
        for i in range(n):
            if not stack: #for day 0 or bigger days
                stack.append(i)
                continue
            if temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
                continue
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx=stack.pop()
                dif=i-idx
                res[idx]=dif
            stack.append(i)
        return res
            