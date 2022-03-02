class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        ans1=[]
        for i in nums:
            if i % 2 == 0:
                ans.append(i)
            else:
                ans1.append(i)
        return ans + ans1 