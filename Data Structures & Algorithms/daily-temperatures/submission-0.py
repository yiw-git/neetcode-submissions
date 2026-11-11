class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [2,1,1,3]
        use a stack [3, 1], [3,2]
        find 1<3:
        stack.pop() question is how to record the distance between the 3 and 1
        so return 3-2
        use another stack to reocrd idx??


        """
        stack=[]
        output=[0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                
                output[stack[-1]]=i-stack[-1]
                stack.pop()
            
            stack.append(i)

        return output



            


                





