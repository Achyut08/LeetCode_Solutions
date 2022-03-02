class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        temp1 = " "
        temp2 = " "
        for i in word1:
            temp1 += i
        print(temp1)
        for i in word2:
            temp2 += i
        print(temp2)
        if temp1 == temp2:
            return True
        else:
            return False