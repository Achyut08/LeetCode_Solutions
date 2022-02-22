class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
         if s == "":
            return True
         if s[0] in t:
            return self.isSubsequence(s[1:], t[t.index(s[0])+1:])
         else:
                return False