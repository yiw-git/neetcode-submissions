class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        print(nums_set)
        count_max=0
        for num in nums_set:
            
            if num-1 in nums_set:
                continue
            else:
                count=0
                while num in nums_set:
                    num+=1
                    count+=1
            if count>=count_max:
                count_max=count

        return count_max

