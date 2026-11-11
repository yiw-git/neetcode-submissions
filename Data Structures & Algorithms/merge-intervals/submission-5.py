class Solution:
    def merge(self, intervals:List[List[int]])-> List[int]:
        intervals.sort(key=lambda x:x[0])
        left, right=intervals[0]
        res=[]

        for start, end in intervals[1:]:
            if start<=right:
                right=max(right, end)
            else:
                res.append([left, right])
                left, right=start, end
        res.append([left, right])
        return res
        # time O(nlonn)--> due to sorting, in place
        #place O(n)
