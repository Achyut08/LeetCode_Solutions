class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #reverse kar ke transpose karenge 
        #transpose matlab swap
        """
        Do not return anything, modify matrix in-place instead.
        """
        
