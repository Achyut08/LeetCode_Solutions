#User function Template for python3


class Solution:
    def factorial (self, n):
        dp = [-1]*(n+1)
        if dp[n] != -1:
            return dp[n]
        if n == 0:
            dp[0] = 1
        elif n == 1:
            dp[1] = 1
        else:
            dp[n] =  n*self.factorial(n-1)
        return dp[n]
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))

# } Driver Code Ends