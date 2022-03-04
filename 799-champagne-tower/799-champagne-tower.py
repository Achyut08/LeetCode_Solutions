class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(102)] for x in range(102)]
        dp[0][0] = poured
        
        for i in range(query_row):
            for j in range(0,i+1):
                flow = (dp[i][j] - 1) / 2.0
                if flow>0:
                    dp[i+1][j] += flow
                    dp[i+1][j+1] += flow
        return min(1,dp[query_row][query_glass])