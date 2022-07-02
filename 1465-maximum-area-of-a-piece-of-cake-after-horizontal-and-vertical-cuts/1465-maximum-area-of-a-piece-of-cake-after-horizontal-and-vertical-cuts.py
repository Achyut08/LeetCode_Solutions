class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mh,mv = 0,0
        hori,verti = sorted(horizontalCuts),sorted(verticalCuts) #getting sorted arrays with easy names
        if len(hori)==1: 
            mh = max(hori[0],h-hori[0])  #Since there is only 1 cut so take max value from both ends of the cake
        else:
            mh = max(hori[0],h-hori[-1])  # difference from the edges from both the cuts at both ends
            for i in range(1,len(hori)):
                mh = max(mh,hori[i]-hori[i-1])  # to get max difference between consecutive cuts
        if len(verti)==1:
            mv = max(verti[0],w-verti[0]) # same as horizintal
        else:
            mv = max(verti[0],w-verti[-1])
            for i in range(1,len(verti)):
                mv = max(mv,verti[i]-verti[i-1])
        return (mh*mv)%1000000007