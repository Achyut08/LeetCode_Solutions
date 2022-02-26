#User function Template for python3
import sys
class Solution:

    def matrixMultiplication(self, N, arr):
        dp = [[-1 for i in range(100)] for j in range(100)]
        def MatrixChainOrder(p, i, j,dp):
            if i == j:
                return 0
            if(dp[i][j] != -1):
                return dp[i][j]
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                dp[i][j] = min(dp[i][j],MatrixChainOrder(p, i, k,dp)+ MatrixChainOrder(p, k + 1, j,dp)+ p[i-1] * p[k] * p[j])
            return dp[i][j]
  
        return MatrixChainOrder(arr,1,N-1,dp)
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends