class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d1={')':'(',']':'[','}':'{'}
        for c in s:
            if c not in d1:
                stack.append(c)
            else:
                if stack and stack[-1]==d1[c]:
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False

