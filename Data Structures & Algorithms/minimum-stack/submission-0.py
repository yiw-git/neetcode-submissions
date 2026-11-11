class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        a=self.stack[-1]
        return a
        
    def getMin(self) -> int:
        min_val=min(self.stack)
        return min_val
        
