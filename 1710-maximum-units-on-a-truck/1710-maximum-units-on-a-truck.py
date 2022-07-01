class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        boxTypes.sort(key = lambda x:-x[1])
        for i in boxTypes:
            no_box = i[0]
            boxunit = i[1]
            if truckSize >= no_box:
                ans += no_box * boxunit
                truckSize -= no_box
                continue
            else:
                ans += truckSize * boxunit
                break
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   