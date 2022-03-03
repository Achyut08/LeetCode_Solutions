class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
        #recursive
    #     res = []
    #     self.backtracking(res,0,[],nums)
    #     return res
    # def backtracking(self,res,start,subset,nums):
    #     res.append(list(subset))
    #     for i in range(start,len(nums)):
    #         subset.append(nums[i])
    #         self.backtracking(res,i+1,subset,nums)
    #         subset.pop()   #push_back
        # #itrative
        # if len(nums) == 0:
        #     return [[]]
        # result = [[]]
        # for x in nums:
        #     n = len(result)
        #     for i in range(n):
        #         r = result[i] + [x]
        #         result.append(r)
        # return result