class Solution(object):
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1 for i in range(n+1)] for i in range(m+1)]
		
        def helper(text1,text2,m,n):
            if m == 0 or n == 0:
                return 0
            if dp[m][n] != -1:
                return dp[m][n]
            if text1[m-1] == text2[n-1]:
                dp[m][n] = 1 + helper(text1,text2,m-1,n-1)
            else:
                dp[m][n] = max(helper(text1,text2,m-1,n),helper(text1,text2,m,n-1))
            return dp[m][n]
        return helper(text1,text2,m,n)
			