class Solution:
    def reverseVowels(self, s: str) -> str:
        v = set('aeiouAEIOU')
        s = list(s)
        l = 0
        r = len(s)-1
        
        while l <= r:
            if s[l] in v and s[r] in v:
                s[l], s[r] = s[r], s[l]
            elif s[r] not in v:
                r -= 1
                continue
            elif s[l] not in v:
                l += 1
                continue
            l += 1
            r -= 1
        
        return ''.join(s)
        
        
     
