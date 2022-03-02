class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def palindromic(word):
            if word == word[::-1]:
                return True
        for i in words:
            if palindromic(i) == True:
                return i
        return ""