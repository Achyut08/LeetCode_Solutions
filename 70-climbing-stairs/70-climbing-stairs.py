class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] *(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] +dp[i-2]
        return dp[n]
        
        
        
        
#         def solve(n):
#             if dp[n] != -1:
#                 return dp[n]
#             if n == 0:
#                 dp[n] = 1
#             elif n == 1:
#                 dp[n] = 1
#             else:
#                 dp[n] = solve(n-1) + solve(n-2)
#             return dp[n]
#         dp = [-1] * (n+1)
#         return solve(n)
    
    
        
        
        
#         self.d = {}
#         return self.climbstair(n)
#     def climbstair(self,n):
#         if n==1:
#             return 1
#         if n==0:
#             return 1
#         if (n) in self.d:
#             return self.d[n]
#         else:
#             self.d[n]= self.climbstair(n-1)+self.climbstair(n-2)
#         return self.d[n]
    