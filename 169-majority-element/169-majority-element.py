class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=sorted(nums)
        n=len(nums)
        mid=len(nums)//2
        return nums[mid]