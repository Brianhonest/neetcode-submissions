class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_counter = 0
        max_num=0
        for i in nums:
            if i == 1:
                num_counter+=1
            else:
                max_num = max(max_num,num_counter)
                num_counter = 0
        return max(max_num, num_counter)