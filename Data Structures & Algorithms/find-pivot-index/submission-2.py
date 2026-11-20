class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = []
        rightSum = []

        total = 0
        for i in nums:
            total+=i
            leftSum.append(total)

        total = 0
        for i in range(len(nums)-1,-1,-1):
            total+=nums[i]
            rightSum.append(total)

        rightSum.reverse()
        for i in range(len(nums)):
            left = leftSum[i-1] if i >0 else 0
            right = rightSum[i+1] if i < len(nums)-1 else 0

            if left == right:
                return i
            
        return -1


                       