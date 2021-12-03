from heapq import *
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        hash_map = {}
        
        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1
            
        max_heap = []
        
        for char, freq in hash_map.items():
            heappush(max_heap, (-freq, char))
            
        prev_char = None
        prev_freq = None
        
        res = []
        
        while max_heap:
            curr_freq, curr_char = heappop(max_heap)
            curr_freq = -(curr_freq)
            res.append(curr_char)
            
            if prev_char is not None and prev_freq > 0:
                heappush(max_heap, (-prev_freq, prev_char))
            
            prev_char = curr_char
            prev_freq = curr_freq - 1
            
            
        
        
        
        
