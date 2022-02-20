class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        exc =0
        inc=0
        n = len(nums)
        print(nums)
        count = [0] *10001
        for i in nums:
            count[i] += 1
        for i in range(0,10000):
            ni = exc+count[i]*i
            ne = max(inc,exc)
            
            inc = ni
            exc = ne
        return max(inc,exc) 