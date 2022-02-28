class Solution:
    #catalan number
    def numTrees(self, n: int) -> int:
        catalan = []
        catalan.append(1)
        for i in range(1,10001):
            x = catalan[i-1]*(4*i-2)/(i+1)
            catalan.append(x)
        return int(catalan[n])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        