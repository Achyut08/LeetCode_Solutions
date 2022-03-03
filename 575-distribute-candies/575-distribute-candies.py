class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ans =  len(candyType)//2
        if len(set(candyType)) >= ans:
            return ans
        else:
            return len(set(candyType))