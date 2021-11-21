class Solution:
    def isPalindrome(self, s: str) -> bool:
#         s = [i for i in s.lower() if i.isalnum()]
#         return s == s[::-1]
    
    #approach 2
          
        new =''
        s = s.lower() # Converts a string to all lower case

        for i in s:
            if i.isalnum(): # is true if the character is an alphanumeric. Meaning alphabets or numbers only. No punctuation, no special characters
                new = new + i

        return new == new[::-1]
