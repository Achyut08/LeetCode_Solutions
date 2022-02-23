class Solution:
    def addDigits(self, num: int) -> int:
        result = 0
        if num <= 9:
            return num
        for i in str(num):
            result += int(i)
        return self.addDigits(result)