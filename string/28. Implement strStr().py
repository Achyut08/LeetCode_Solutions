class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        if needle in haystack:
            res = haystack.index(needle)
        return res
