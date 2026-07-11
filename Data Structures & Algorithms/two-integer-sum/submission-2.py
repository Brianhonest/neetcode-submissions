class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        intmap = {}

        for i,n  in enumerate(nums):
            diff = target - n
            if diff in intmap:
                return  [intmap[diff],i]
            intmap[n]=i