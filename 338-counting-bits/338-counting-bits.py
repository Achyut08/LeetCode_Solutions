class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num+1):
            count=0
            n=i
            while(n):
                n=n&(n-1)
                count += 1
            counter.append(count)
        return counter
            
        