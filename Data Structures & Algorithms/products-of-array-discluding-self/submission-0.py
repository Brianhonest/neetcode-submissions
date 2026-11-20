class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        productList = []
        productListRight = []
        
        for i in nums:
            productList.append(product)
            product*=i

        product= 1
        for n in range(len(nums)-1,-1,-1):
            productListRight.append(product)
            product*=nums[n]

        productListRight.reverse()

        for i in range(len(nums)):
            productList[i]*=productListRight[i]

        return productList
