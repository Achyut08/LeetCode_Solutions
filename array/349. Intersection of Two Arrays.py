class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)
        return res
