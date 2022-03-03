class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        6
        mid = n // 2
        sum1 = 0
        for i in range(n):
            sum1 += mat[i][i]
            sum1 += mat[i][n-1-i]
        if n % 2 == 1:
            sum1 -= mat[mid][mid]
        return sum1