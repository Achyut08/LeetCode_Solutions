class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = 0
        for i in range(len(nums)):
            if reach < i:
                return False
            reach =max(reach,i+nums[i])
        return True
#         max_size=0
#         for i in range(len(nums)):
#             if (nums[i]+i > max_size):
#                 max_size=nums[i]+i
#             if (max_size==i):
#                 break
#         return max_size >= len(nums)-1
        