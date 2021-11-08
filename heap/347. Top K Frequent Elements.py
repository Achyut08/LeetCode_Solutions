from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num]+=1
        for key, val in dict.items():
            if len(min_heap) < k:
                heappush(min_heap, (val,key))
            else:
                heappushpop(min_heap, (val,key))
        res = [x[1] for x in min_heap]
        return res
