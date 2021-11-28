class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def hcf(a,b):
            if b == 0:
                return a
            else:
                return hcf(b,a%b)
        a=min(nums)
        b=max(nums)
        return hcf(a,b)
        
