class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = []
        for i in nums:
            if i == 1:
                count += 1
            if i == 0:
                ans.append(count)
                count = 0
        ans.append(count)
        print(ans)
        return max(ans)