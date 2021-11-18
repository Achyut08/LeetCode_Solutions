class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list((set(range(1,len(nums)+1)))-(set(nums)))
#2nd approach
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:    
        lenn = len(nums)
        for i in range(lenn):
            val = abs(nums[i]) - 1
            nums[val] = abs(nums[val]) * -1
        res = []
        for i in range(lenn):
            if nums[i] > 0:
                res.append(i+1)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
