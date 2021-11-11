class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d={"a":".-",
           "b":"-...",
           "c":"-.-.",
           "d":"-..",
           "e":".",
           "f":"..-.",
           "g":"--.",
           "h":"....",
           "i":"..",
           "j":".---",
           "k":"-.-",
           "l":".-..",
           "m":"--",
           "n":"-.",
           "o":"---",
          "p":".--.",
           "q":"--.-",
           "r":".-.",
           "s":"...",
           "t":"-",
           "u":"..-",
           "v":"...-",
           "w":".--",
           "x":"-..-",
           "y":"-.--",
           "z":"--.."}
        ans=set()
        for word in words:
            cw=""
            for char in word:
                cw = cw + d[char]
            ans.add(cw)
        return len(ans)
