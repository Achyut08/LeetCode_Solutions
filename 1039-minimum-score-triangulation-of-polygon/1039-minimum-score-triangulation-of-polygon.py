class Solution:
    import math
    def minScoreTriangulation(self, values: List[int]) -> int:
        def mcm(values,i,j,dp):
            if i == j:
                dp[i][j] = 0
            if dp[i][j] != -1:
                return dp[i][j]
            min_val = math.inf
            for k in range(i,j):
                temp_val = mcm(values,i,k,dp) + mcm(values,k+1,j,dp) + values[i-1] * values[k] * values[j]
                if temp_val < min_val:
                    min_val = temp_val
                    dp[i][j] = min_val
            return min_val
        dp = [[-1] * len(values) for i in range(len(values))]
        ans = mcm(values,1,len(values) - 1,dp)
        return ans