#{ 
#Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


 # } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,nums, target):
        nums = sorted(list(set(nums)))
        res = []
        self.backtracking(res,0,[],nums,target)
        return res
    def backtracking(self,res,start,subset,nums,target):
        if (start == len(nums)):
            if target == 0:
                res.append(list(subset))
            return
        if nums[start] <= target:
            subset.append(nums[start])
            self.backtracking(res,start,subset,nums,target-nums[start])
            subset.pop() 
        self.backtracking(res,start+1,subset,nums,target)
    #     arr.sort()
    #     res = []
    #     self.backtracking(res,0,[],arr,target)
    #     return res
    # def backtracking(self,res,index,subset,arr,target):
    #     if index == len(arr):
    #         if target == 0:
    #             res.append(list(subset))
    #         return
    #     if arr[index] <= target:
    #         subset.append(arr[index])
    #         self.backtracking(res,index,subset,arr,target-arr[index])
    #         subset.pop()
    #     self.backtracking(res,index+1,subset,arr,target)

        # code here

#{ 
#Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

#} Driver Code Ends