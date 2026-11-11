class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        """
        search for k
        the range of k is [1, max(pile)]

        want to search k. for each possible k, caluclate the hours needed
        hours+=ceil(p/k)
        hours+=(p+k-1)//k
        k--> [1, 2, 3, 4, maxpile]
        the possible k is a range, not a single value but want the left-most one

        """
        left=1
        right=max(piles)
        while left<=right:
            mid=(left+right)//2
            hours=0
            for pile in piles:
                hours+=(pile+mid-1)//mid
            if hours>h:
                left=mid+1
            else:
                right=mid-1
        return left
            

