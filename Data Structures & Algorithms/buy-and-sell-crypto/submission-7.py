class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#[5,6,1,4,3]
#pointer1=buy, go from idx 0 to end
#pointer2=sell, gofrom idx 1 to end
        p1=0
        p2=1
        profit=0

        while p2<len(prices):
            if p1<p2 and prices[p1]<prices[p2]:
                profit=max(profit, prices[p2]-prices[p1])
            if p1<p2 and prices[p1]>=prices[p2]:
                p1=p2
            p2+=1
        return profit






        