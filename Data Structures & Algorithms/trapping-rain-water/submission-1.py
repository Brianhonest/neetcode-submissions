
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        currMax=height[0]
        maxLeft = []

        for i in height:
            currMax = max(currMax,i)
            maxLeft.append(currMax)

        maxRight=[]
        currMaxRight = height[-1]

        for i in range(len(height)-1,-1,-1):
            currMaxRight = max(currMaxRight,height[i])
            maxRight.append(currMaxRight)

        maxRight.reverse()
        total = 0
        for i in range(len(height)):
            minHeight = min(maxRight[i],maxLeft[i])
            total+=abs(minHeight-height[i])
        
        return total
