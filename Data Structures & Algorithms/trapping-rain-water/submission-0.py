class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        left_max=0
        right_max=0
        area=0

        while left<right:
            left_max=max(left_max,height[left])
            right_max=max(right_max, height[right])
            if height[left]<height[right]:
                area+=min(left_max, right_max)-height[left]
                left+=1
                
            else:
                area+=min(left_max, right_max)-height[right]
                right-=1
        return area
            


            
            
            



            

