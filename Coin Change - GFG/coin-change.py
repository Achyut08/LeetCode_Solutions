#User function Template for python3

class Solution:
    def solve(self,s,n,cap):
        if cap==0:
            return 1
        if n==0:
            return 0
        if (n,cap) in self.d:
            return self.d[(n,cap)]
        if s[n-1]>cap:
            c1=self.solve(s,n-1,cap)
            self.d[(n,cap)]=c1
            return c1
        else:
            c1=self.solve(s,n,cap-s[n-1])
            c2=self.solve(s,n-1,cap)
            self.d[(n,cap)]=c1+c2
            return c1+c2
    def count(self, s, m, n): 
        self.d={}
        return self.solve(s,m,n)
        
        # code here 


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends