class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #f(12)=a
        #f(12)=min(f(11)+1, f(7)+1, f(2)+1)
        #f(i)=min(f(i),min(f(i-1), f(i-5), f(i-10))+1)
        if amount==0:
            return 0
        l1=[float('inf')]*(amount+1)
        #l2=-float('inf')
        l1[0]=0
        
        for coin in coins:
            if coin<=amount:
                l1[coin]=1
        
        for i in range(amount+1):
            candidate=float('inf')
            for coin in coins:
                if i>=coin:
                    candidate=min(candidate, l1[i-coin]+1)
            l1[i]=min(l1[i], candidate)
        if l1[-1]!=float('inf'):
            return l1[-1]
        else:
            return -1
        #l1[1]=1 if 1 in coins else -1
        #l1[1]=min(min(f(1-coin1),f(1-coin2), ... f(1-coink))+1, l1[1])
        #bottom up
        #l1[2]=

        


        



