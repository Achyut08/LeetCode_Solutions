#User function Template for python3


class Solution:
    def factorial (self, n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return n*self.factorial(n-1)
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