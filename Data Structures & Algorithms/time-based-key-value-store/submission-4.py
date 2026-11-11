class TimeMap:

    def __init__(self):
        self.info={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.info:
            self.info[key]=[(value, timestamp)]
        else:
            self.info[key].append((value, timestamp))
         

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.info:
            return ""
        alice=self.info[key]

        left=0
        right=len(alice)-1
        value=""
        while left<=right:
            mid=(left+right)//2

            if timestamp==alice[mid][1]:
                #return alice[mid][0]#problem is the alice[mid][0] is none
                return alice[mid][0]
                
            if timestamp>alice[mid][1]:
                value=alice[mid][0]
                left=mid+1
            else:
                right=mid-1
        return value

        
    
        
        
