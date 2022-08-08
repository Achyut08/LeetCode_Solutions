class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]                  
        for i in range(2,n):
            for j in range(n-i):
                k = j+i
                for l in range(j+1,k):
                    dp[j][k] = max(dp[j][k] , nums[j]*nums[l]*nums[k] + dp[j][l] + dp[l][k])
        return dp[0][n-1]
                    