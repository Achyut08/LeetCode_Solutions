from collections import Counter
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ans = []
        for i in rectangles:
            ans.append(min(i))
        ans = Counter(ans)
        return ans[max(ans)]