from heapq import *
class Solution:
    def kClosest(self, point: List[List[int]], k: int) -> List[List[int]]:
        max_heap=[]
        new=[]
        for i in range(len(point)):
            dist=(point[i][0]*point[i][0])+(point[i][1]*point[i][1])
            heappush(max_heap,(-dist,(point[i][0],point[i][1])))
            if len(max_heap)>k:
                heappop(max_heap)
        for i in range(len(max_heap)):
            new.append(max_heap[i][1])
        return new
