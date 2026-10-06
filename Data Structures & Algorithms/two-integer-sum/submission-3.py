class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_={}
        
        for i,n in enumerate(nums):
            value = target-n
            if value in sum_:
                return [sum_[value],i]
            sum_[n]=i

            