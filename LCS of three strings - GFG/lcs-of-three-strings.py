#User function Template for python3

class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        def lcs(X,Y,Z,m,n,o):
            L = [[[0 for i in range(o+1)] for j in range(n+1)]for k in range(m+1)]
            for i in range(m+1):
                for j in range(n+1):
                    for k in range(o+1):
                        if (i == 0 or j == 0 or k == 0):
                            L[i][j][k] = 0
                     
                        elif (X[i-1] == Y[j-1] and X[i-1] == Z[k-1]):
                            L[i][j][k] = L[i-1][j-1][k-1] + 1
 
                        else:
                            L[i][j][k] = max(max(L[i-1][j][k],L[i][j-1][k]),L[i][j][k-1])
            return L[m][n][o]
        return lcs(A,B,C,len(A),len(B),len(C))
                
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n1,n2,n3 = map(int,input().split())
        A,B,C = input().split()

        solObj = Solution()

        ans = solObj.LCSof3(A,B,C,n1,n2,n3)

        print(ans)
# } Driver Code Ends