class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h = len(grid)
        w= len(grid[0])
        if h == 0:
            return 0
        if w == 0:
            return 0
        count = 0
        for i in range(0,h):
            for j in range(0,w):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
            
        return count

    def dfs(self,grid: List[List[str]],i,j):
        grid[i][j] = '0'
        if (i+1 < len(grid) and grid[i+1][j] == '1'):
            self.dfs(grid,i+1,j)
        if (i-1 >= 0 and grid[i-1][j] == '1'):
            self.dfs(grid,i-1,j)
        if (j-1 >= 0 and grid[i][j-1] == '1'):
            self.dfs(grid,i,j-1)
        if (j+1 < len(grid[0]) and grid[i][j+1] == '1'):
            self.dfs(grid,i,j+1)
      
            