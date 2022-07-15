class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row0 = len(matrix) *[False]
        col0 = len(matrix[0]) *[False]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row0[i] = True
                    col0[j] = True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row0[i] or col0[j]:
                    matrix[i][j] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
        