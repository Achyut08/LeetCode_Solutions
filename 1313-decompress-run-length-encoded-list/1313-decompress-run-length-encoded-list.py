class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = len(nums)
        a=[]
        for i in range(0,l,2):
            a.extend(nums[i]*[nums[i+1]])
        return a
        
        
        
        
        
        
    