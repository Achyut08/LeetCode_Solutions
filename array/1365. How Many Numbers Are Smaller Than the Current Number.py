class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]< nums[i] and j!=i:
                    count += 1
            res.append(count)
            count = 0
        return res
