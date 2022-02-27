# Sort the List to get the top 3 lengths
# Check if the largest length is less than sum of other two
# If 2 is false, drop the max length take next 3 largest length and repeat 1-2
# if 2 is true, return sum of all lengths
# if loop ends, and no possible combination found, return 0
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse = True)
        for i in range(3,len(A)+1):
            if(A[i-3] < A[i-2] + A[i-1]):
                return sum(A[i-3:i])
        return 0