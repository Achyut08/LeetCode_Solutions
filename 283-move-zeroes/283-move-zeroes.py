class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[l] == 0:
                nums[l], nums[i] = nums[i], nums[l]

            # wait while we find a non-zero element to
            # swap with you
            if nums[l] != 0:
                l += 1
            
        """
        Do not return anything, modify nums in-place instead.
        """
        