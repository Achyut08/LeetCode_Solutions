# you may use python module's
# just return true/false or 1/0
class Solution():
    def isPowerofFour(self, n):
        if n == 1:
            return True
        if n <= 0 or n%4 != 0:
            return False
        return self.isPowerofFour(n//4)
         # code here

#{ 
#  Driver Code Starts
# Your code goes here

if __name__=='__main__':
    test = int(input())
    for i in range(test):
        num = int(input())
        if(Solution().isPowerofFour(num)):
            print (1)
        else:
            print (0)
# } Driver Code Ends