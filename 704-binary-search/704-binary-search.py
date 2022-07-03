class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = nums[0]
        high = len(nums)-1
        if nums is None:
            return -1
        if nums[0] == target:
            return 0
        if nums[len(nums)-1] == target:
            return len(nums) -1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1