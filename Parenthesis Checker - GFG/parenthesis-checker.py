
#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,s):
        stack = []
        
        # loop over the string
        for char in s:
            
            # if we find any opening bracket then we push it on the stack
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
                
            # This statement only gets triggered when the string starts with closing bracket eg: },),]
            elif not stack:
                return False
            
            # if we find any closing bracket after pushing to the stack we check if it's equal to the last pushed char
            # if it is we pop it off the stack if not then we return False
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
            
            
        # in the end if all closing brackets are found then stack will be empty
        return len(stack) == 0
     
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends