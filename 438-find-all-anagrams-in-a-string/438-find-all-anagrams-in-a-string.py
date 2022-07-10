class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        counter_p = Counter(p)
        counter_s = Counter(s[0:len_p])
        
        start_index_array = []
        
        for i in range(len_s - len_p+1):
            
            if counter_s== counter_p:
                start_index_array.append(i)
                
            counter_s[s[i]]-= 1
            
            if i!=len_s-len_p:
                counter_s[s[i+len_p]]+= 1
            
                
        return start_index_array