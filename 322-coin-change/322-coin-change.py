class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        nrows = len(coins) + 1
        ncols = amount + 1
        
        dp = [[2**64 for _ in range(ncols)] for _ in range(nrows)]
        for i in range(nrows):
            dp[i][0] = 0
        for i in range(1, nrows):
            for j in range(1, ncols):
                if j < coins[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    include = 1 + dp[i][j - coins[i - 1]]
                    exclude = dp[i - 1][j]
                    dp[i][j] = min(include, exclude)
                    
        if dp[-1][-1] == 2**64:
            return -1
        else:
            return dp[-1][-1]