class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        l1=[0]*(n+1)
        l1[1]=1
        l1[2]=2
        for i in range(3, n+1):
            l1[i]=l1[i-1]+l1[i-2]
        return l1[n]