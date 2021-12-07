class Solution:
    def isHappy(self, n: int) -> bool:
        s= set()
        print(s)
        s.add(n)
        print(s)
        
        while True:
            
            n=sum([int(i)**2 for i in str(n)])
            print(n)
            
            if n==1:
                return True
            
            if n in s:
                return False
            
            s.add(n)
