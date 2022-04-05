class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        i, j = 0, len(height)-1
        while (i < j):
            width = min(height[i], height[j])
            area = width * (j - i)
            result = max(result, area)
            if height[i]<height[j]: i+=1
            else: j -= 1
        return result