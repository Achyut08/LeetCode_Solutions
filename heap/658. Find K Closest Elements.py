from heapq import *
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap=[]
        new=[]
        for i in range(len(arr)):
            diff=abs(arr[i]-x)
            heappush(max_heap,(-diff,-arr[i]))
            if len(max_heap)>k:
                heappop(max_heap)
        for i in range(len(max_heap)):
            new.append(-max_heap[i][1])
        new.sort()
        return new
            
        
        
