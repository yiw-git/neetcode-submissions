class Solution:

    def encode(self, strs: List[str]) -> str:

#strs=["12.", "abc","#1#2","1#1"]
#encoder: 3#  3#   4#     3# 
#str: 3#12.3#abc
        if not strs:
            return ""

        encoded_str=""
        for s in strs:
            s_new=str(len(s))+"#"+s
            encoded_str+=s_new
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        """
        sizes, res, i=[], [], 0
        while s[i]!='#':
            j=i
            while s[j]!=',':
                j+=1
            sizes.append(int(s[i:j]))
            i=j+1

        i+=1
        for sz in sizes:
            res.append(s[i:i+sz])
            i+=sz
        return res

        """
        strs=[]
        sub_str=""
        sub_len=0
        start_idx=0
        end_idx=0

        while start_idx<len(s):
            end_idx=start_idx
            while s[end_idx]!="#":
                end_idx+=1
            sub_len=int(s[start_idx:end_idx])
            sub_str=s[end_idx+1:end_idx+1+sub_len]
            strs.append(sub_str)
            start_idx=end_idx+sub_len+1

        return strs
"""
            if int(s[start_idx])==0:
                start_idx+=2
            else:
                end_idx=start_idx+int(s[start_idx])+2
                substr=s[start_idx+2:end_idx]
                strs.append(substr)

                start_idx=end_idx+1
                """





