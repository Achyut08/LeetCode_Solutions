class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1 = 0
        maxi = nums[0]
        for i in range(len(nums)):
            if sum1 < 0:
                sum1 = 0
            sum1 += nums[i]
            maxi = max(maxi,sum1)
        return maxi