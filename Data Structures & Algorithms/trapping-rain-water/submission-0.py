
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        total = 0
        currMax = height[0]
        maxLeft = []

        currMaxRight = height[-1]
        maxRight = []

        # Find maximum height from the left
        for r in height:
            currMax = max(currMax, r)
            maxLeft.append(currMax)

        # Find maximum height from the right
        for l in range(len(height) - 1, -1, -1):
            currMaxRight = max(currMaxRight, height[l])
            maxRight.append(currMaxRight)

        maxRight.reverse()

        # Calculate trapped rainwater
        for i in range(len(height)):
            minHeight = min(maxLeft[i], maxRight[i])
            total += minHeight - height[i]

        return total
