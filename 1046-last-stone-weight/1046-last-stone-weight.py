class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for i in range(len(stones)):
            heappush(max_heap,-stones[i])
        while len(max_heap) > 1:
            x = -heappop(max_heap)
            y = -heappop(max_heap)
            if x != y:
                temp = abs(x-y)
                heappush(max_heap,-temp)
            else:
                continue
        if max_heap:
            return -max_heap[0]
        else:
            return 0
    
    
   
        # return -stones[-1] if stones else 0