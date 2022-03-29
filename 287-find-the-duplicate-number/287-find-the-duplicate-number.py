class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
#         slow=nums[0]
#         fast=nums[0]
#         slow=nums[slow]
#         fast=nums[nums[fast]]
#         while(slow!=fast):
#             sow=nums[slow]
#             fast=nums[nums[fast]]
#         fast=nums[0]
#         while(fast!=slow):
#             slow=nums[slow]
#             fast=nums[fast]
#         return fast
        
        
        
            
        