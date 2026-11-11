class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position)==0:
            return 0
        dec_list=list(zip(position, speed))
        dec_list.sort(reverse=True)

        times=[]
        for i in dec_list:
            times.append((target-i[0])/i[1])

        stack=[]
        stack.append(times[0])
        
        for j in range(1,len(times)):
            if times[j]>stack[-1]:
                stack.append(times[j])
            
        return len(stack)

        