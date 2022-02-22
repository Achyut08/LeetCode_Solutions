#User function Template for python3

class Solution:

    def longestPalinSubseq(self, s):
        def lcs(x,y):
            n=len(x)
            dp = [[None]*(n+1) for _ in range(n+1)]
            
            for i in range(n+1):
                for j in range(n+1):
                    if i==0 or j==0:
                        dp[i][j]=0
                    elif x[i-1]==y[j-1]:
                        dp[i][j]=1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return dp[-1][-1]
        return lcs(s,s[::-1])
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends