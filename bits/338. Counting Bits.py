class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num+1):
            counter.append(counter[i >> 1] + i % 2)
            return counter
        
#2nd approach
class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num+1):
            count=0
            n=i
            while(n):
                count += 1
                n=n&(n-1)
            counter.append(count)
        return counter
            
        