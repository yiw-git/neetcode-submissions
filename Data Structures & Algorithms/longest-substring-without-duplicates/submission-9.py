class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=1
        txt=""
        if len(s)==0:
            return 0
        max_len=1

        txt=s[left]
        while right<len(s):

            while s[right] in txt:
                txt=txt[1:]
                left+=1

            txt+=s[right]
            max_len=max(max_len, len(txt))
            right+=1
        return max_len


