class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        res=0
        for n in nums:
            if n in num_set:
                num_set.remove(n)
                prev,next=n-1,n+1
                while prev in num_set:
                    num_set.remove(prev)
                    prev -= 1
                while next in num_set:
                    num_set.remove(next)
                    next += 1
                res = max(res,next-prev-1)
        return res
            
