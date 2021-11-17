class Solution:
    def binaryGap(self, n: int) -> int:
        temp=0
        maxdis=0
        dis=0
        while n>0:
            if n&1:
                temp=1 
                maxdis=max(maxdis,dis)
                dis=1
            elif temp==1:
                dis += 1
            n = n>> 1
        return maxdis
                
