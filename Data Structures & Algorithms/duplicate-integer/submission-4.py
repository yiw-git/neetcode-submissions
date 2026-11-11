class Solution:
    def hasDuplicate(self, nums:List[int])-> bool:
        new_nums=set(nums)
        if len(nums)==len(new_nums):
            return False
        else:
            return True
        
        
        """
        set1=set()
        for num in nums:
            if num in set1:
                return True
            set1.add(num)
        return False
        """


