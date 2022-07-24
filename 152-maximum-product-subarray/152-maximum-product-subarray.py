class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        cprod = 1
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            cprod *= nums[i]
            ans = max(ans,cprod)
            if cprod == 0:
                cprod = 1
        cprod = 1
        for i in range(len(nums)-1,-1,-1):
            cprod *= nums[i]
            ans = max(ans,cprod)
            if cprod == 0:
                cprod = 1
        return ans