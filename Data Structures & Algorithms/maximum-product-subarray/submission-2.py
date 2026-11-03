class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)

        currMin,currMax = 1,1

        for i in nums:
            if i ==0:
                currMin,currMax=1,1
                continue
            tmp = currMax*i
            currMax=max(i*currMax,i*currMin,i)
            currMin = min(tmp,i*currMin,i)
            res = max(res,currMax)
        return res