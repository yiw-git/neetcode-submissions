class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        """
        when to update p2, when max_val_len+k>=sub_len:
        update p2
        while <
        update p1 
        """
        p1=0
        count={}

        max_len=0
        
        max_freq=0

        for p2 in range(len(s)):
            count[s[p2]]=count.get(s[p2],0)+1
            max_freq=max(max_freq, count[s[p2]])
            
            while max_freq+k<p2-p1+1:
                print("p1, and s[p1]", p1, s[p1])
                count[s[p1]]-=1
                p1+=1

            max_len=max(max_len, p2-p1+1)
    
        return max_len



