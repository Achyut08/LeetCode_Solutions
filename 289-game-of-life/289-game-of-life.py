class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len( board[0])
        dp = []
        
        for i in range (m):
            tp = []
            for j in range (n):
                tp.append(board[i][j])
            dp.append(tp)
        
        for i in range (m):
            for j in range (n):
                ct = 0
                if i > 0:
                    if board[i-1][j] == 1:
                        ct += 1
                    if j > 0:
                        if board[i-1][j-1] == 1:
                            ct += 1
                    if j < n-1:
                        if board[i-1][j+1] == 1:
                            ct += 1
                if j > 0:
                    if board[i][j-1] == 1:
                        ct += 1
                if j < n-1:
                    if board[i][j+1] == 1:
                        ct += 1
                        
                if i < m-1:
                    if board[i+1][j] == 1:
                            ct += 1
                    if j > 0:
                        if board[i+1][j-1] == 1:
                            ct += 1
                    if j < n-1:
                        if board[i+1][j+1] == 1:
                            ct += 1           
                dp[i][j] = ct
        
        for i in range (m):
            for j in range (n):
                if board[i][j] == 1:
                    if dp[i][j] < 2:
                        board[i][j] = 0
                    elif dp[i][j] > 3:
                        board[i][j] = 0
                elif board[i][j] == 0:
                    if dp[i][j] == 3:
                        board[i][j] = 1
            print( dp[i])
        return board
        