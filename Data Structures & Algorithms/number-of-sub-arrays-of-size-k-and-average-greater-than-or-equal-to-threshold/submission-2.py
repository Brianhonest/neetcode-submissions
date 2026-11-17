class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = 0
        l = 0
        total = 0
        for r in range(len(arr)):
            currSum += arr[r]
            if r-l+1 > k :
                currSum -=arr[l]
                l+=1

            if r-l+1 == k:
                if currSum >= threshold*k:
                    total+=1
        return total
