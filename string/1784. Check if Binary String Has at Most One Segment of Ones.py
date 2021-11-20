class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        isValid = True
        for i in range(len(s)):
            
            if s[i] == "1":
                if not isValid:
                    return False
            else:
                isValid = False
        
        return True
