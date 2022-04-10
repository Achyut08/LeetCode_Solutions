class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
            m=len(grid1)
            n=len(grid1[0])

            def dfs(i,j):
                if i<0 or i>=m or j<0 or j>=n or grid2[i][j]==0 or (i,j) in visited:
                    return

                visited.add((i,j))
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i-1,j)

            visited=set()
            for i in range(m):
                for j in range(n):
                    if grid2[i][j]==1 and grid1[i][j]==0:
                        dfs(i,j)

            res=0
            
            for i in range(m):
                for j in range(n):
                    if grid2[i][j]==1 and (i,j) not in visited:
                        dfs(i,j)
                        res+=1
            return res

