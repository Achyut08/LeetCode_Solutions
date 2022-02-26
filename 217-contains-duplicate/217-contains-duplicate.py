class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap=set()
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap.add(nums[i])
        