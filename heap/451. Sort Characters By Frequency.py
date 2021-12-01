from heapq import *
class Solution:
    def frequencySort(self, string: str) -> str:
	    frequency_map = dict()

	    for char in string:
		    frequency_map[char] = frequency_map.get(char, 0) + 1

	    max_heap = []

	    for char, frequency in frequency_map.items():
		    heappush(max_heap, (-frequency, char))

	    sorted_string = []

	    while max_heap:
		    frequency, char = heappop(max_heap)
		    for i in range(-frequency):
			    sorted_string.append(char)

	    return ''.join(sorted_string)
