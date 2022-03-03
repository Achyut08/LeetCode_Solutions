class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtracking(res,0,[],nums,target)
        return res
    def backtracking(self,res,start,subset,nums,target):
        if (start == len(nums)):
            if target == 0:
                res.append(list(subset))
            return
        if nums[start] <= target:
            subset.append(nums[start])
            self.backtracking(res,start,subset,nums,target-nums[start])
            subset.pop() 
        self.backtracking(res,start+1,subset,nums,target)