class Solution:
    def fib(self, n: int) -> int:
        def solve(n):
            if dp[n] != -1:
                return dp[n]
            if n == 0:
                dp[n] = 0
            elif n == 1:
                dp[n] = 1
            else:
                dp[n] = solve(n-1) + solve(n-2)
            return dp[n]
        dp = [-1] * (n+1)
        return solve(n)
    
    
    
#     class Solution:
#     def fib(self, N: int) -> int:      
#         def dp(n):
#             if memo[n] != None:
#                 return memo[n]
#             memo[n] = 0 if n==0 else 1 if n == 1 else dp(n-1) + dp(n-2)
#             return memo[n]  
        
#         memo = [None] * (N+1)
#         return dp(N)