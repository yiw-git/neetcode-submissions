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
        if len(s)!=len(t):
            return False

        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1

        for a in t:
            if a not in count:
                return False
            
            count[a]-=1
            if count[a]==0:
                del count[a]



        


        return len(count)==0


