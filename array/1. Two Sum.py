class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countener={}
        for i,num in enumerate(nums):
            if target-num in countener:
                return [countener[target-num],i]
            countener[num]=i
        
        
