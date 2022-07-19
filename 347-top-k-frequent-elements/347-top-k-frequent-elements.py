class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        hashmap = {}
        for item in nums:
            if item in hashmap:
                hashmap[item] += 1
            else:
                hashmap[item] = 1
        print(hashmap)
        for num,count in hashmap.items():
            heappush(min_heap,(count,num))
            if len(min_heap) > k:
                heappop(min_heap)
        result = []
        for i in range(len(min_heap)):
            result.append(min_heap[i][1])
        return result
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         num_map = {}
#         min_heap = [] # We use a min heap so that we can keep K values in it, and when we have more than
#         #k values we pop off the smallest, keeping the largest K
        
#         # Populate map with frequency of each number O(n)
#         for num in nums:
#             if num not in num_map:
#                 num_map[num] = 0he
#             num_map[num] += 1
        
#         # Iterate through items in map, appending to min_heap and popping of the smallest when it gets
#         # larger than K. O(nlogK)
#         for num, count in num_map.items():
#             heapq.heappush(min_heap, (count, num))
#             if len(min_heap) > k:
#                 heapq.heappop(min_heap)
                
#         # Append the num, not the count, from the min_heap to result O(n)
#         result = []
#         for i in range(len(min_heap)):
#             result.append(min_heap[i][1])
        
#         return result
        
        
        
        
        
        
        