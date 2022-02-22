class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
         
        def lcs(x,y):
            n=len(x)
            dp = [[None]*(n+1) for _ in range(n+1)]
            
            for i in range(n+1):
                for j in range(n+1):
                    if i==0 or j==0:dp[i][j]=0
                    elif x[i-1]==y[j-1]:dp[i][j]=1+dp[i-1][j-1]
                    else:dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            #for i in dp:print(i)
            return dp[-1][-1]
        return lcs(s,s[::-1])