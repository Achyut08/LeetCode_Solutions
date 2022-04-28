
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums=collections.Counter(arr)
        s=set()    
        for i in arr:
            s.add(nums[i])
        if len(nums)!=len(s):
            return False
        else:
            return True