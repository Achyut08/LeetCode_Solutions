class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row,col = len(matrix),len(matrix[0])
        cache ={}
        
        def solve(r,c):
            if r >= row or c>= col:
                return 0
            
            if (r,c) not in cache:
                down = solve(r+1,c)
                right = solve(r,c+1)
                diag = solve(r+1,c+1)
                
                cache[(r,c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down,right,diag)
            return cache[(r,c)]
        solve(0,0)
        return max(cache.values()) **2