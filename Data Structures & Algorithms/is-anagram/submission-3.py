class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        1 how to convert the string into list
        s1=[]
        for i in s:
            s1.append(i)
        t1=[]
        for i in t:
            t1.append(i)

        s2=s1.sort()
        t2=s1.sort()
        if s2==t2:
            return True
        return False
        a=set()
        but set cannot hold duplicates 

        """
        return sorted(s)==sorted(t)


