class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadan's algorithm
        sums=0
        maximun=nums[0]
        for i in nums:
            if sums<0:
                sums=0
            sums += i
            maximun=max(sums,maximun)
        return maximun
        