#User function Template for python3

class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        def solve(text1,text2,m,n):
            t = [[0]*(n+1) for i in range(m+1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if text1[i-1] == text2[j-1]:
                        t[i][j] = t[i-1][j-1] + 1
                    else:
                        t[i][j] = max(t[i][j - 1], t[i - 1][j])
            return t[m][n]
        return m+n-solve(X,Y,m,n)
        
        
         #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends