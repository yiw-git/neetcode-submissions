class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
"ABCDEFGDHIJK"
A-p1, B-p2

p2 to ahead to G (p2 less than end and p2 not in txt)

now next p2 is D is duplicates in  tt.
so p1 move to B, and while loop to iterate until p2 is not in the txt
"AAB"
"""
        p1=0
        p2=1
        if s=="":
            return 0
        txt=s[p1]
        max_len=1

        while p2<len(s):
            if s[p2] not in txt:
                txt+=(s[p2])
                
                p2+=1
            else:
                while s[p2] in txt: 
                    txt=txt[1:]
                    p1+=1
            max_len=max(len(txt), max_len)
        return max_len


