class Solution:
    def maximumWealth(self, nums: List[List[int]]) -> int:
        sum1=0
        for i in range(len(nums)):
            sum2=sum(nums[i])
            sum1=max(sum1,sum2)
        return sum1
        
        
   
