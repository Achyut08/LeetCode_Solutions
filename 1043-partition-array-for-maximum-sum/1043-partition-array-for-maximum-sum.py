class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [None] * (len(arr) + 1)
        dp[0] = 0
        for i in range(1, len(arr) + 1):
            candidate = []
            for j in range(1, k+1):
                if i-j >= 0 and i-j < len(arr):

                    candidate.append(dp[i-j] + max(arr[i-j:i])*j)
            
            dp[i] = max(candidate)
        return dp[-1]