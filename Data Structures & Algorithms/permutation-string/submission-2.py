class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        left=0
        right=len(s1)-1
        
        count={}
        count1={}
        for i in range(len(s1)):
            count[s2[i]]=count.get(s2[i],0)+1
        for i in range(len(s1)):
            count1[s1[i]]=count1.get(s1[i],0)+1
        if count==count1:
            return True

        while right<len(s2)-1:
            count[s2[left]]-=1
            if count[s2[left]] == 0:
                del count[s2[left]]
            left+=1            
            right+=1
            count[s2[right]]=count.get(s2[right],0)+1
            if count==count1:
                return True


        return False



