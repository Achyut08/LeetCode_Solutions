class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None:
            return None
        row = len(matrix)
        col = len(matrix[0])
        low = 0 
        high = (row * col)-1
        while(low <= high):
            mid  = low + (high-low) //2
            midele = matrix[mid//col][mid%col]
            if (midele == target):
                return True
            if (midele < target):
                low = mid + 1
            else:
                high = mid - 1 
        return False