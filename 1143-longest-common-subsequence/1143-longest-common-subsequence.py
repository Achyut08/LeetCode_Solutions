class Solution(object):
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        n, m = len(A), len(B)
        dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + A[i]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
        #print(dp)
        return (len(dp[-1][-1]))
#         m = len(text1)
#         n = len(text2)
#         dp = [[-1 for i in range(n+1)] for i in range(m+1)]
		
#         def helper(text1,text2,m,n):
#             if m == 0 or n == 0:
#                 return 0
#             if dp[m][n] != -1:
#                 return dp[m][n]
#             if text1[m-1] == text2[n-1]:
#                 dp[m][n] = 1 + helper(text1,text2,m-1,n-1)
#             else:
#                 dp[m][n] = max(helper(text1,text2,m-1,n),helper(text1,text2,m,n-1))
#             return dp[m][n]
#         return helper(text1,text2,m,n)
			
        
        
#         m = len(text1)
#         n = len(text2)
#         dp = [[-1 for i in range(n+1)] for j in range(m+1)]
#         def solve(text1,text2,m,n):
#             if n == 0 or m == 0:
#                 return 0
#             if dp[m][n] != -1:
#                 return dp[m][n]
#             if text1[m-1] == text2[n-1]:
#                 dp[m][n] = 1 + solve(text1,text2,m-1,n-1)
#             else:
#                 dp[m][n] = max(solve(text1,text2,m,n-1),solve(text1,text2,m-1,n))
#             return dp[m][n]
#         return solve(text1,text2,m,n)



			