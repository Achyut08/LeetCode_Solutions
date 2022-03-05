#User function Template for python3

class Solution:
    def nQueen(self, n):
        board = [[0 for _ in range(n)]for _ in range(n)]
        res = []
        helper(board, 0, [], res, n)
        return res
        
        
def isSafe(row,col,board,n):
    #checking vertical direction
    i = row - 1
    while i >= 0:
        if board[i][col] == 1:
            return False
        i = i - 1
    #checking  north-west
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1
    #checking  north-east
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
    return True


def helper(board, row, path, res, n):
    if len(path) == n:
        res.append(path)
        return

    for col in range(n):
        if isSafe(row,col,board, n):
            board[row][col] = 1
            helper(board, row+1, path+[col+1], res, n)
            board[row][col] = 0
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends