class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        intmap = {}
        for num in nums:
            if num in intmap:
                return True
            else:
                intmap[num] = 1

        return False